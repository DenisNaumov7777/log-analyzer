import re
import csv
import logging
from collections import Counter
from pathlib import Path
from typing import List, Pattern
from dataclasses import dataclass, asdict


logger = logging.getLogger(__name__)

@dataclass
class LogEntry:
    timestamp: str
    host: str
    service: str
    level: str
    message: str

@dataclass
class ErrorStat:
    message: str
    count: int

class EnterpriseLogAnalyzer:
    def __init__(self, log_path: str | Path):
        self.log_path: Path = Path(log_path)
        self.entries: List[LogEntry] = []
        
        # Pre-compiled Regex
        self.log_pattern: Pattern = re.compile(
            r"(?P<timestamp>\w{3}\s+\d+\s\d+:\d+:\d+)\s+"
            r"(?P<host>\S+)\s+"
            r"(?P<service>[\w\[\]\-\.=]+):\s+"
            r"(?P<level>[A-Z]+)\s+"
            r"(?P<message>.+)"
        )

    def analyze(self) -> None:
        if not self.log_path.exists():
            
            logger.error(f"Input file not found: {self.log_path}")
            raise FileNotFoundError(f"File not found: {self.log_path}")

        logger.info(f"Starting analysis logic for: {self.log_path}")

        try:
            with self.log_path.open("r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    # Fast-path optimization
                    if "ERROR" not in line:
                        continue

                    match = self.log_pattern.search(line)
                    if not match or match.group("level") != "ERROR":
                        continue

                    entry = LogEntry(
                        timestamp=match.group("timestamp"),
                        host=match.group("host"),
                        service=match.group("service"),
                        level=match.group("level"),
                        message=match.group("message").strip(),
                    )
                    self.entries.append(entry)

            logger.info(f"Analysis complete. Extracted {len(self.entries)} records.")

        except Exception as e:
            logger.critical(f"Critical failure in analyzer core: {e}")
            raise

    def get_top_errors(self, limit: int = 5) -> List[ErrorStat]:
        counter = Counter(e.message for e in self.entries)
        return [ErrorStat(msg, count) for msg, count in counter.most_common(limit)]

    def export_csv(self, output_path: str) -> None:
        logger.info(f"Writing CSV report to: {output_path}")
        try:
            stats = self.get_top_errors(limit=100) # Export all stats
            with open(output_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Count", "Error Message"])
                for stat in stats:
                    writer.writerow([stat.count, stat.message])
        except IOError as e:
            logger.error(f"Failed to write CSV: {e}")
            raise
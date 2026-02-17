import argparse
import sys
import yaml
import logging.config
from pathlib import Path


from src.analyzer import EnterpriseLogAnalyzer

def setup_logging(config_path="logging.yaml"):
    """Load logging configuration from YAML file."""
    path = Path(config_path)
    if path.exists():
        with open(path, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        
        logging.basicConfig(level=logging.INFO)
        logging.warning("logging.yaml not found. Using default config.")

def main():
    
    setup_logging()
    logger = logging.getLogger("MainApp") 

    
    parser = argparse.ArgumentParser(
        description="Syslog Insight: Enterprise-grade log analysis tool."
    )
    
    parser.add_argument(
        "--input", "-i", 
        type=str, 
        required=True, 
        help="Path to the input log file (e.g., data/syslog.log)"
    )
    parser.add_argument(
        "--output", "-o", 
        type=str, 
        default="error_report.csv", 
        help="Path to the output CSV report (default: error_report.csv)"
    )

    args = parser.parse_args()

    logger.info(f"Application started. Input: {args.input}")

    try:
        
        analyzer = EnterpriseLogAnalyzer(args.input)
        analyzer.analyze()
        
        
        print("\n" + "="*40)
        print(f"TOP CRITICAL ERRORS REPORT")
        print("="*40)
        
        top_errors = analyzer.get_top_errors(5)
        
        if not top_errors:
            print("✅ No errors found. System is healthy.")
        else:
            print(f"{'COUNT':<6} | {'MESSAGE'}")
            print("-" * 40)
            for stat in top_errors:
                print(f"{stat.count:<6} | {stat.message[:60]}...") 
        
        print("="*40 + "\n")

        
        analyzer.export_csv(args.output)
        logger.info("Task finished successfully.")

    except FileNotFoundError:
        logger.error("The specified input file does not exist.")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
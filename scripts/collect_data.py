"""
Data Collection Script
Collects and generates all competitive intelligence data
"""

import sys
from pathlib import Path

from src.config import PROCESSED_DATA_DIR

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from data_collector import CompetitiveDataCollector
from config import *


def main():
    print("=" * 80)
    print(" DATA COLLECTION SCRIPT")
    print("=" * 80)
    print()
    
    print(f"Product: {PRODUCT_NAME}")
    print(f"Collecting data for {len(COMPETITORS)} competitors")
    print()
    
    # Initialize collector
    collector = CompetitiveDataCollector()
    
    # Generate all data
    print("Step 1: Generating competitive overview...")
    collector.generate_competitive_overview()
    
    print("\nStep 2: Generating feature matrix...")
    collector.generate_feature_matrix()
    
    print("\nStep 3: Generating traffic estimates...")
    collector.generate_traffic_estimates()
    
    print("\nStep 4: Generating user reviews...")
    collector.generate_user_reviews()
    
    # Save all data
    print("\n" + "-" * 80)
    print("Saving data to disk...")
    print("-" * 80)
    collector.save_all_data()
    
    print("\n" + "=" * 80)
    print(" DATA COLLECTION COMPLETE")
    print("=" * 80)
    print()
    print(f"✅ All data saved to: {PROCESSED_DATA_DIR}")
    print()
    print("Next steps:")
    print("  1. Review generated CSV files in data/processed/")
    print("  2. Run analysis: python scripts/run_full_analysis.py")
    print("  3. Or generate reports: python scripts/generate_report.py")
    print()


if __name__ == "__main__":
    main()
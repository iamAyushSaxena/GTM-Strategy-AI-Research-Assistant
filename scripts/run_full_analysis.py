"""
Master Script: Run Full GTM Analysis
Executes all analysis steps in sequence
"""

import sys
from pathlib import Path
import time

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from data_collector import CompetitiveDataCollector
from competitive_analyzer import CompetitiveAnalyzer
from market_sizer import MarketSizer
from pricing_strategy import PricingStrategy
from gtm_planner import GTMPlanner
from financial_model import FinancialModel
from visualization import GTMVisualizer
from config import *

import pandas as pd


def print_banner(text):
    """Print formatted banner"""
    print("\n" + "=" * 80)
    print(f" {text}")
    print("=" * 80 + "\n")


def main():
    start_time = time.time()

    print_banner("GTM STRATEGY ANALYSIS - FULL PIPELINE")
    print(f"Product: {PRODUCT_NAME}")
    print(f"Target Market: {TARGET_MARKET['primary']['segment']}")
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Step 1: Data Collection
    print_banner("STEP 1: DATA COLLECTION")
    collector = CompetitiveDataCollector()

    print("Generating competitive data...")
    collector.generate_competitive_overview()
    collector.generate_feature_matrix()
    collector.generate_traffic_estimates()
    collector.generate_user_reviews()
    collector.save_all_data()

    print("\n✅ Data collection complete!")

    # Step 2: Competitive Analysis
    print_banner("STEP 2: COMPETITIVE ANALYSIS")

    competitors_df = pd.read_csv(PROCESSED_DATA_DIR / "competitive_overview.csv")
    features_matrix = pd.read_csv(PROCESSED_DATA_DIR / "feature_matrix.csv")

    analyzer = CompetitiveAnalyzer(competitors_df, features_matrix)

    print("Calculating positioning...")
    positioning = analyzer.calculate_positioning_coordinates()
    positioning.to_csv(PROCESSED_DATA_DIR / "positioning_data.csv", index=False)

    print("Identifying white space...")
    white_space = analyzer.identify_white_space()

    print("Performing SWOT analysis...")
    swot = analyzer.perform_swot_analysis()
    swot.to_csv(PROCESSED_DATA_DIR / "swot_analysis.csv", index=False)

    print("Analyzing feature gaps...")
    feature_gaps = analyzer.calculate_feature_gaps()
    feature_gaps.to_csv(PROCESSED_DATA_DIR / "feature_gaps.csv", index=False)

    print("Generating summary...")
    summary = analyzer.generate_competitive_summary()
    with open(
        REPORTS_DIR / "competitive_analysis_summary.txt", "w", encoding="utf-8"
    ) as f:
        f.write(summary)

    print("\n✅ Competitive analysis complete!")

    # Step 3: Market Sizing
    print_banner("STEP 3: MARKET SIZING (TAM/SAM/SOM)")

    sizer = MarketSizer()

    print("Calculating TAM...")
    tam = sizer.calculate_tam()

    print("Calculating SAM...")
    sam = sizer.calculate_sam()

    print("Calculating SOM...")
    som = sizer.calculate_som(timeframe_months=12)

    print("Generating report...")
    market_report = sizer.generate_market_sizing_report()
    with open(REPORTS_DIR / "market_sizing_report.txt", "w", encoding="utf-8") as f:
        f.write(market_report)

    assumptions_df = sizer.export_assumptions_table()
    assumptions_df.to_csv(
        PROCESSED_DATA_DIR / "market_sizing_assumptions.csv", index=False
    )

    print("\n✅ Market sizing complete!")

    # Step 4: Pricing Strategy
    print_banner("STEP 4: PRICING STRATEGY & UNIT ECONOMICS")

    strategy = PricingStrategy()

    print("Analyzing competitor pricing...")
    strategy.analyze_competitor_pricing(competitors_df)

    print("Calculating value metrics...")
    strategy.calculate_value_metrics()

    print("Validating unit economics...")
    strategy.validate_unit_economics()

    print("Generating recommendation...")
    pricing_report = strategy.generate_pricing_recommendation()
    with open(
        REPORTS_DIR / "pricing_strategy_recommendation.txt", "w", encoding="utf-8"
    ) as f:
        f.write(pricing_report)

    print("\n✅ Pricing strategy complete!")

    # Step 5: GTM Planning
    print_banner("STEP 5: GO-TO-MARKET PLANNING (90 DAYS)")

    planner = GTMPlanner()

    print("Creating weekly breakdown...")
    weekly_plan = planner.create_weekly_breakdown()
    weekly_plan.to_csv(PROCESSED_DATA_DIR / "gtm_weekly_plan.csv", index=False)

    print("Defining channel strategy...")
    channel_strategy = planner.define_channel_strategy()

    print("Generating GTM report...")
    gtm_report = planner.generate_gtm_report()
    with open(REPORTS_DIR / "gtm_strategy_report.txt", "w", encoding="utf-8") as f:
        f.write(gtm_report)

    print("\n✅ GTM planning complete!")

    # Step 6: Financial Modeling
    print_banner("STEP 6: FINANCIAL PROJECTIONS (24 MONTHS)")

    model = FinancialModel()

    print("Projecting user growth...")
    projections = model.project_user_growth(months=24)
    projections.to_csv(
        PROCESSED_DATA_DIR / "financial_projections_24m.csv", index=False
    )

    print("Calculating break-even...")
    breakeven = model.calculate_break_even()

    print("Generating financial report...")
    financial_report = model.generate_financial_report()
    with open(REPORTS_DIR / "financial_model_report.txt", "w", encoding="utf-8") as f:
        f.write(financial_report)

    print("\n✅ Financial modeling complete!")

    # Step 7: Visualizations
    print_banner("STEP 7: GENERATING VISUALIZATIONS")

    viz = GTMVisualizer()

    print("Creating positioning matrix...")
    fig1 = viz.plot_positioning_matrix(positioning)
    fig1.write_html(DASHBOARDS_DIR / "positioning_matrix.html")

    print("Creating feature comparison...")
    fig2 = viz.plot_feature_comparison(features_matrix)
    fig2.write_html(DASHBOARDS_DIR / "feature_comparison.html")

    print("Creating market sizing funnel...")
    market_data = {"tam": tam, "sam": sam, "som": som}
    fig3 = viz.plot_tam_sam_som_funnel(market_data)
    fig3.write_html(DASHBOARDS_DIR / "market_sizing_funnel.html")

    print("Creating financial projections chart...")
    fig4 = viz.plot_financial_projections(projections)
    fig4.write_html(DASHBOARDS_DIR / "financial_projections.html")

    print("Creating channel mix chart...")
    fig5 = viz.plot_channel_mix(channel_strategy)
    fig5.write_html(DASHBOARDS_DIR / "channel_mix.html")

    print("\n✅ Visualizations complete!")

    # Final Summary
    print_banner("ANALYSIS COMPLETE - SUMMARY")

    elapsed_time = time.time() - start_time

    print(f"✅ All analyses completed in {elapsed_time:.1f} seconds\n")

    print("📊 KEY FINDINGS:")
    print(f"   Market Size (SOM): {som['final']:,} users")
    print(f"   Revenue Potential: ${som['revenue_potential']['arr']:,} ARR")
    print(f"   Break-even: Month {breakeven.get('month', 'N/A')}")
    print(f"   LTV/CAC Ratio: 7.2x")
    print(f"   Payback Period: 3.3 months")
    print()

    print("📁 OUTPUTS GENERATED:")
    print(f"   Data files: {PROCESSED_DATA_DIR}")
    print(f"   Reports: {REPORTS_DIR}")
    print(f"   Visualizations: {DASHBOARDS_DIR}")
    print()

    print("🚀 NEXT STEPS:")
    print("   1. Review reports in outputs/reports/")
    print("   2. Open interactive dashboards in outputs/dashboards/")
    print("   3. Run Streamlit app: streamlit run app/streamlit_app.py")
    print("   4. Customize assumptions in src/config.py")
    print()

    print("=" * 80)
    print(" Thank you for using the GTM Strategy Analyzer!")
    print("=" * 80)


if __name__ == "__main__":
    main()

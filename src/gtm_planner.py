"""
Go-to-Market (GTM) Planner
90-day launch plan with tactics and metrics
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from config import *


class GTMPlanner:
    """
    Creates detailed 90-day go-to-market roadmap
    """

    def __init__(self):
        self.roadmap = GTM_ROADMAP
        self.weekly_plan = None
        self.channel_strategy = None

    def create_weekly_breakdown(self) -> pd.DataFrame:
        """
        Break down 90-day plan into weekly tasks
        """
        print("📅 Creating weekly GTM breakdown...")

        weekly_tasks = []
        start_date = datetime.now()

        # Phase 1: Days 1-30 (Weeks 1-4)
        phase1_weeks = [
            {
                "week": 1,
                "phase": "Phase 1: Private Beta",
                "focus": "Beta Recruitment",
                "tasks": [
                    "Post beta signup on Academic Twitter",
                    "Share in r/PhD, r/GradSchool subreddits",
                    "Email 50 PhD students from personal network",
                    "Set up beta waitlist landing page",
                    "Create onboarding email sequence",
                ],
                "metrics": {"signups": 30, "interviews": 5},
                "budget": 500,
            },
            {
                "week": 2,
                "phase": "Phase 1: Private Beta",
                "focus": "First User Cohort",
                "tasks": [
                    "Onboard first 30 beta users",
                    "Conduct 5 user interviews",
                    "Fix critical bugs from feedback",
                    "Ship 2 feature improvements",
                    "Start NPS tracking",
                ],
                "metrics": {"activation_rate": 0.35, "bugs_fixed": 8},
                "budget": 1000,
            },
            {
                "week": 3,
                "phase": "Phase 1: Private Beta",
                "focus": "Product Iteration",
                "tasks": [
                    "Recruit 40 more beta users",
                    "Implement top 3 feature requests",
                    "Optimize onboarding flow",
                    "Create case study: PhD student lit review",
                    "Build referral mechanism",
                ],
                "metrics": {"signups": 70, "activation_rate": 0.40},
                "budget": 1500,
            },
            {
                "week": 4,
                "phase": "Phase 1: Private Beta",
                "focus": "PMF Validation",
                "tasks": [
                    "Final beta cohort (30 users)",
                    "NPS survey to all users",
                    "Calculate retention metrics",
                    "Validate pricing with survey",
                    "Prepare Product Hunt launch materials",
                ],
                "metrics": {"total_users": 100, "nps": 40, "retention_day7": 0.40},
                "budget": 2000,
            },
        ]

        # Phase 2: Days 31-60 (Weeks 5-8)
        phase2_weeks = [
            {
                "week": 5,
                "phase": "Phase 2: Public Launch",
                "focus": "Launch Prep",
                "tasks": [
                    "Finalize Product Hunt submission",
                    "Record demo video (2 min)",
                    "Write 10 SEO blog posts",
                    "Set up Google Analytics & Mixpanel",
                    "Prepare launch day social media content",
                ],
                "metrics": {"content_pieces": 10, "demo_video": 1},
                "budget": 3000,
            },
            {
                "week": 6,
                "phase": "Phase 2: Public Launch",
                "focus": "Product Hunt Launch",
                "tasks": [
                    "Launch on Product Hunt (Tuesday 8am PST)",
                    "Monitor comments & respond within 1 hour",
                    "Post on HackerNews, Reddit, Twitter",
                    "Email all beta users for support",
                    "Run Reddit AMA on r/PhD",
                ],
                "metrics": {"signups": 500, "product_hunt_rank": 1, "upvotes": 800},
                "budget": 5000,
            },
            {
                "week": 7,
                "phase": "Phase 2: Public Launch",
                "focus": "SEO Foundation",
                "tasks": [
                    "Publish 5 more SEO articles",
                    "Guest post on ResearchGate blog",
                    "Start backlink outreach (50 sites)",
                    'Optimize site for "AI research tools" keywords',
                    "Set up email nurture campaign",
                ],
                "metrics": {"signups": 200, "organic_traffic": 1000},
                "budget": 4000,
            },
            {
                "week": 8,
                "phase": "Phase 2: Public Launch",
                "focus": "Partnership Development",
                "tasks": [
                    "Reach out to 10 university research labs",
                    "Partner with Academia.edu newsletter",
                    "Create affiliate program (20% commission)",
                    "Attend virtual research conference",
                    "Launch referral program (1 month free)",
                ],
                "metrics": {"signups": 300, "partnerships": 2},
                "budget": 3000,
            },
        ]

        # Phase 3: Days 61-90 (Weeks 9-12)
        phase3_weeks = [
            {
                "week": 9,
                "phase": "Phase 3: Paid Acquisition",
                "focus": "Google Ads Launch",
                "tasks": [
                    "Set up Google Ads campaigns",
                    'Target keywords: "AI literature review tool"',
                    "A/B test 3 ad creatives",
                    "Set daily budget: $200",
                    "Track CAC by keyword",
                ],
                "metrics": {"signups": 400, "cac": 50},
                "budget": 6000,
            },
            {
                "week": 10,
                "phase": "Phase 3: Paid Acquisition",
                "focus": "Conversion Optimization",
                "tasks": [
                    "A/B test landing page (3 variants)",
                    "Optimize signup flow (reduce friction)",
                    "Implement exit-intent popup",
                    "Add social proof (testimonials)",
                    "Improve free-to-paid conversion triggers",
                ],
                "metrics": {"signups": 500, "conversion_rate": 0.09},
                "budget": 8000,
            },
            {
                "week": 11,
                "phase": "Phase 3: Paid Acquisition",
                "focus": "Influencer & PR",
                "tasks": [
                    "Partner with 3 academic YouTubers",
                    "Pitch to TechCrunch, The Verge",
                    'Sponsor podcast: "The Academic Life"',
                    "Run Twitter Ads (promoted tweets)",
                    "Create comparison guides vs competitors",
                ],
                "metrics": {"signups": 600, "media_mentions": 2},
                "budget": 10000,
            },
            {
                "week": 12,
                "phase": "Phase 3: Paid Acquisition",
                "focus": "Scale & Optimize",
                "tasks": [
                    "Scale Google Ads budget to $400/day",
                    "Launch retargeting campaigns",
                    "Analyze cohort retention trends",
                    "Calculate unit economics by channel",
                    "Prepare Series A fundraising deck",
                ],
                "metrics": {"signups_total": 5000, "paying": 500, "mrr": 7500},
                "budget": 6000,
            },
        ]

        # Combine all weeks
        all_weeks = phase1_weeks + phase2_weeks + phase3_weeks

        for week_data in all_weeks:
            week_num = week_data["week"]
            week_start = start_date + timedelta(weeks=week_num - 1)
            week_end = week_start + timedelta(days=6)

            weekly_tasks.append(
                {
                    "week": week_num,
                    "start_date": week_start.strftime("%Y-%m-%d"),
                    "end_date": week_end.strftime("%Y-%m-%d"),
                    "phase": week_data["phase"],
                    "focus": week_data["focus"],
                    "tasks": "; ".join(week_data["tasks"]),
                    "num_tasks": len(week_data["tasks"]),
                    "budget_usd": week_data["budget"],
                    "key_metrics": str(week_data["metrics"]),
                }
            )

        self.weekly_plan = pd.DataFrame(weekly_tasks)

        print(f"✅ Created 12-week GTM plan")
        print(f"   Total budget: ${self.weekly_plan['budget_usd'].sum():,}")
        print(f"   Total tasks: {self.weekly_plan['num_tasks'].sum()}")

        return self.weekly_plan

    def define_channel_strategy(self) -> Dict:
        """
        Define acquisition channel strategy and ROI
        """
        print("📡 Defining channel strategy...")

        channels = {
            "product_hunt": {
                "name": "Product Hunt",
                "type": "Launch Platform",
                "expected_users": 800,
                "cac": 20,
                "budget": 5000,
                "timeline": "Week 6",
                "tactics": [
                    "Launch Tuesday 8am PST",
                    "Prepare maker story & demo video",
                    "Engage community day before",
                    "Respond to all comments within 1 hour",
                ],
                "success_criteria": "#1 Product of the Day, 800+ upvotes",
            },
            "seo_content": {
                "name": "SEO & Content Marketing",
                "type": "Organic",
                "expected_users": 1200,
                "cac": 15,
                "budget": 10000,
                "timeline": "Weeks 5-12",
                "tactics": [
                    "Publish 20 high-quality articles",
                    'Target keywords: "AI research tools", "literature review software"',
                    "Guest posts on academic blogs",
                    "Build backlinks from .edu sites",
                ],
                "success_criteria": "500+ organic visitors/week by Month 3",
            },
            "google_ads": {
                "name": "Google Ads (Search)",
                "type": "Paid",
                "expected_users": 1500,
                "cac": 50,
                "budget": 25000,
                "timeline": "Weeks 9-12",
                "tactics": [
                    "Target high-intent keywords",
                    "A/B test ad copy & landing pages",
                    "Retargeting campaigns",
                    "Budget: $200-400/day scaling",
                ],
                "success_criteria": "CAC < $50, Conversion rate > 8%",
            },
            "referrals": {
                "name": "Referral Program",
                "type": "Viral",
                "expected_users": 600,
                "cac": 10,
                "budget": 3000,
                "timeline": "Weeks 3-12",
                "tactics": [
                    "1 month free for 3 successful referrals",
                    "In-app referral prompts",
                    "Email templates for sharing",
                    "Track viral coefficient",
                ],
                "success_criteria": "Viral coefficient > 0.3",
            },
            "social_media": {
                "name": "Social Media (Twitter, Reddit)",
                "type": "Community",
                "expected_users": 500,
                "cac": 25,
                "budget": 8000,
                "timeline": "Weeks 1-12",
                "tactics": [
                    "Academic Twitter engagement",
                    "Reddit AMAs (r/PhD, r/GradSchool)",
                    "Share user success stories",
                    "Behind-the-scenes building",
                ],
                "success_criteria": "2000+ engaged followers by Month 3",
            },
            "partnerships": {
                "name": "Academic Partnerships",
                "type": "B2B",
                "expected_users": 400,
                "cac": 30,
                "budget": 4000,
                "timeline": "Weeks 7-12",
                "tactics": [
                    "ResearchGate, Academia.edu newsletters",
                    "University library partnerships",
                    "Research lab pilots",
                    "Academic conference presence",
                ],
                "success_criteria": "3+ partnerships, 400+ users",
            },
        }

        # Calculate blended metrics
        total_users = sum(ch["expected_users"] for ch in channels.values())
        total_budget = sum(ch["budget"] for ch in channels.values())
        blended_cac = total_budget / total_users if total_users > 0 else 0

        channel_summary = {
            "channels": channels,
            "summary": {
                "total_expected_users": total_users,
                "total_budget": total_budget,
                "blended_cac": blended_cac,
                "channels_count": len(channels),
            },
            "channel_mix": {
                ch_name: {
                    "users_percentage": ch["expected_users"] / total_users,
                    "budget_percentage": ch["budget"] / total_budget,
                }
                for ch_name, ch in channels.items()
            },
        }

        self.channel_strategy = channel_summary

        print(f"✅ Defined {len(channels)} acquisition channels")
        print(f"   Total expected users: {total_users:,}")
        print(f"   Total budget: ${total_budget:,}")
        print(f"   Blended CAC: ${blended_cac:.2f}")

        return channel_summary

    def generate_gtm_report(self) -> str:
        """
        Generate comprehensive GTM strategy report
        """
        if self.weekly_plan is None:
            self.create_weekly_breakdown()

        if self.channel_strategy is None:
            self.define_channel_strategy()

        report = "=" * 80 + "\n"
        report += "90-DAY GO-TO-MARKET STRATEGY\n"
        report += "=" * 80 + "\n\n"

        report += "🎯 EXECUTIVE SUMMARY\n"
        report += "-" * 80 + "\n"
        report += f"Total Duration: 90 days (12 weeks)\n"
        report += f"Total Budget: ${self.weekly_plan['budget_usd'].sum():,}\n"
        report += f"Target Users: {self.channel_strategy['summary']['total_expected_users']:,}\n"
        report += f"Target Paying Customers: {SUCCESS_METRICS['monetization']['free_to_paid']['target'] * self.channel_strategy['summary']['total_expected_users']:.0f}\n"
        report += f"Target MRR: ${SUCCESS_METRICS['monetization']['free_to_paid']['target'] * self.channel_strategy['summary']['total_expected_users'] * PRICING_TIERS['pro']['price_monthly']:.0f}\n"
        report += f"\n\n"

        report += "📅 PHASE BREAKDOWN\n"
        report += "-" * 80 + "\n"
        for phase_name, phase_data in GTM_ROADMAP.items():
            report += f"\n{phase_data['name'].upper()}\n"
            report += f"   Duration: {phase_data['duration']}\n"
            report += f"   Budget: ${phase_data['budget']:,}\n"
            report += f"   Goals:\n"
            for goal in phase_data["goals"]:
                report += f"      • {goal}\n"
            report += f"\n   Key Tactics:\n"
            for tactic in phase_data["tactics"][:3]:  # Top 3
                report += f"      • {tactic}\n"
            report += f"\n   Success Metrics:\n"
            for metric, value in phase_data["metrics"].items():
                if isinstance(value, float):
                    report += f"      • {metric}: {value*100:.1f}%\n"
                else:
                    report += f"      • {metric}: {value:,}\n"

        report += "\n\n"
        report += "📡 ACQUISITION CHANNELS\n"
        report += "-" * 80 + "\n"
        for ch_name, ch_data in self.channel_strategy["channels"].items():
            report += f"\n{ch_data['name']} ({ch_data['type']})\n"
            report += f"   Expected Users: {ch_data['expected_users']:,}\n"
            report += f"   CAC: ${ch_data['cac']}\n"
            report += f"   Budget: ${ch_data['budget']:,}\n"
            report += f"   Timeline: {ch_data['timeline']}\n"
            report += f"   Success: {ch_data['success_criteria']}\n"

        report += "\n\n"
        report += "📊 WEEK-BY-WEEK ROADMAP\n"
        report += "-" * 80 + "\n"
        for _, week in self.weekly_plan.iterrows():
            report += f"\nWEEK {week['week']}: {week['focus']}\n"
            report += f"   Phase: {week['phase']}\n"
            report += f"   Budget: ${week['budget_usd']:,}\n"
            report += f"   Tasks: {week['num_tasks']} tasks\n"

        report += "\n\n"
        report += "✅ SUCCESS CRITERIA (90-Day Targets)\n"
        report += "-" * 80 + "\n"
        report += f"Total Sign-ups: {SUCCESS_METRICS['acquisition']['total_signups']['target']:,}\n"
        report += f"Activated Users: {SUCCESS_METRICS['activation']['signup_to_first_synthesis']['target'] * SUCCESS_METRICS['acquisition']['total_signups']['target']:.0f}\n"
        report += f"Paying Customers: {SUCCESS_METRICS['monetization']['free_to_paid']['target'] * SUCCESS_METRICS['acquisition']['total_signups']['target']:.0f}\n"
        report += f"Monthly Recurring Revenue: ${SUCCESS_METRICS['monetization']['free_to_paid']['target'] * SUCCESS_METRICS['acquisition']['total_signups']['target'] * PRICING_TIERS['pro']['price_monthly']:,.0f}\n"
        report += f"Day-7 Retention: {SUCCESS_METRICS['activation']['day_7_retention']['target']*100:.0f}%\n"
        report += f"NPS: {SUCCESS_METRICS['north_star']['target']}\n"

        return report


if __name__ == "__main__":
    print("=" * 80)
    print(" GTM STRATEGY PLANNER")
    print("=" * 80)
    print()

    planner = GTMPlanner()

    # Create weekly plan
    weekly_plan = planner.create_weekly_breakdown()

    # Define channel strategy
    channel_strategy = planner.define_channel_strategy()

    # Generate report
    report = planner.generate_gtm_report()
    print("\n" + report)

    # Save outputs
    weekly_plan.to_csv(PROCESSED_DATA_DIR / "gtm_weekly_plan.csv", index=False)

    with open(REPORTS_DIR / "gtm_strategy_report.txt", "w") as f:
        f.write(report)

    print("\n💾 Outputs saved")
    print("✅ GTM strategy planning complete!")

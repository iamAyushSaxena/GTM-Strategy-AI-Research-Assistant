"""
Data Collector for Competitive Analysis
Generates synthetic competitive intelligence data
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List
from config import *

np.random.seed(42)


class CompetitiveDataCollector:
    """
    Collects and generates competitive intelligence data
    """
    
    def __init__(self):
        self.competitors_df = None
        self.features_matrix = None
        self.traffic_data = None
        self.reviews_data = None
        
    def generate_competitive_overview(self) -> pd.DataFrame:
        """
        Generate comprehensive competitor overview
        """
        print("📊 Generating competitive overview...")
        
        competitors_list = []
        
        for key, comp in COMPETITORS.items():
            competitors_list.append({
                'competitor_id': key,
                'name': comp['name'],
                'description': comp['description'],
                'founded_year': comp['founded'],
                'ai_added_year': comp['ai_added'],
                'positioning': comp['positioning'],
                'pricing_free': comp['pricing'].get('free', False),
                'pricing_lowest': min([v for v in comp['pricing'].values() if isinstance(v, (int, float))]),
                'estimated_users': comp['users_estimate'],
                'total_funding_usd': comp['funding_total'],
                'latest_valuation_usd': comp.get('latest_valuation', 0)
            })
        
        self.competitors_df = pd.DataFrame(competitors_list)
        
        print(f"✅ Generated data for {len(self.competitors_df)} competitors")
        return self.competitors_df
    
    def generate_feature_matrix(self) -> pd.DataFrame:
        """
        Generate feature comparison matrix
        """
        print("🔧 Generating feature comparison matrix...")
        
        # Define feature availability for each competitor (0-10 scale)
        # 0 = Not available, 10 = Best-in-class
        
        feature_scores = {
            'notion_ai': {
                'AI Summarization': 8,
                'Cross-source Synthesis': 4,
                'Knowledge Graph Visualization': 3,
                'Automatic Linking': 7,
                'Collaboration': 10,
                'Academic Database Integration': 2,
                'Citation Management': 1,
                'Version History': 9,
                'Mobile App': 8,
                'Offline Mode': 6,
                'API Access': 8,
                'Custom AI Prompts': 6,
                'Export Options': 9,
                'Search Quality': 7,
                'Privacy (Local-first)': 2
            },
            'mem_ai': {
                'AI Summarization': 9,
                'Cross-source Synthesis': 6,
                'Knowledge Graph Visualization': 7,
                'Automatic Linking': 9,
                'Collaboration': 4,
                'Academic Database Integration': 1,
                'Citation Management': 0,
                'Version History': 5,
                'Mobile App': 7,
                'Offline Mode': 3,
                'API Access': 5,
                'Custom AI Prompts': 7,
                'Export Options': 6,
                'Search Quality': 9,
                'Privacy (Local-first)': 3
            },
            'reflect': {
                'AI Summarization': 7,
                'Cross-source Synthesis': 5,
                'Knowledge Graph Visualization': 8,
                'Automatic Linking': 8,
                'Collaboration': 3,
                'Academic Database Integration': 0,
                'Citation Management': 0,
                'Version History': 8,
                'Mobile App': 6,
                'Offline Mode': 5,
                'API Access': 4,
                'Custom AI Prompts': 5,
                'Export Options': 7,
                'Search Quality': 7,
                'Privacy (Local-first)': 6
            },
            'obsidian': {
                'AI Summarization': 6,  # Via plugins
                'Cross-source Synthesis': 3,
                'Knowledge Graph Visualization': 9,
                'Automatic Linking': 10,
                'Collaboration': 5,
                'Academic Database Integration': 4,  # Via Zotero plugin
                'Citation Management': 5,
                'Version History': 10,  # Git integration
                'Mobile App': 8,
                'Offline Mode': 10,
                'API Access': 7,  # Plugin API
                'Custom AI Prompts': 8,
                'Export Options': 10,
                'Search Quality': 8,
                'Privacy (Local-first)': 10
            },
            'roam': {
                'AI Summarization': 5,
                'Cross-source Synthesis': 4,
                'Knowledge Graph Visualization': 10,
                'Automatic Linking': 9,
                'Collaboration': 6,
                'Academic Database Integration': 2,
                'Citation Management': 3,
                'Version History': 7,
                'Mobile App': 5,
                'Offline Mode': 4,
                'API Access': 6,
                'Custom AI Prompts': 4,
                'Export Options': 6,
                'Search Quality': 6,
                'Privacy (Local-first)': 4
            },
            'napkin_ai': {
                'AI Summarization': 7,
                'Cross-source Synthesis': 3,
                'Knowledge Graph Visualization': 10,  # Visual diagrams
                'Automatic Linking': 5,
                'Collaboration': 3,
                'Academic Database Integration': 0,
                'Citation Management': 0,
                'Version History': 4,
                'Mobile App': 4,
                'Offline Mode': 2,
                'API Access': 3,
                'Custom AI Prompts': 6,
                'Export Options': 7,
                'Search Quality': 5,
                'Privacy (Local-first)': 2
            },
            'recall': {
                'AI Summarization': 8,
                'Cross-source Synthesis': 7,
                'Knowledge Graph Visualization': 8,
                'Automatic Linking': 9,
                'Collaboration': 2,
                'Academic Database Integration': 3,
                'Citation Management': 2,
                'Version History': 4,
                'Mobile App': 6,
                'Offline Mode': 3,
                'API Access': 4,
                'Custom AI Prompts': 6,
                'Export Options': 6,
                'Search Quality': 8,
                'Privacy (Local-first)': 3
            }
        }
        
        # Add our product (ResearchFlow AI)
        feature_scores['our_product'] = {
            'AI Summarization': 9,
            'Cross-source Synthesis': 10,  # Our differentiator
            'Knowledge Graph Visualization': 9,
            'Automatic Linking': 9,
            'Collaboration': 5,  # V1 focus on individual
            'Academic Database Integration': 10,  # Deep integration
            'Citation Management': 10,  # Export to BibTeX, RIS
            'Version History': 7,
            'Mobile App': 6,  # V2 priority
            'Offline Mode': 4,
            'API Access': 7,
            'Custom AI Prompts': 8,
            'Export Options': 9,
            'Search Quality': 8,
            'Privacy (Local-first)': 5
        }
        
        # Convert to DataFrame
        matrix_data = []
        for competitor_id, scores in feature_scores.items():
            for feature, score in scores.items():
                matrix_data.append({
                    'competitor_id': competitor_id,
                    'feature': feature,
                    'score': score
                })
        
        self.features_matrix = pd.DataFrame(matrix_data)
        
        print(f"✅ Generated feature matrix: {len(FEATURE_DIMENSIONS)} features × {len(feature_scores)} products")
        return self.features_matrix
    
    def generate_traffic_estimates(self) -> pd.DataFrame:
        """
        Generate traffic estimates (SimilarWeb-style data)
        """
        print("📈 Generating traffic estimates...")
        
        traffic_data = []
        
        for key, comp in COMPETITORS.items():
            # Estimate monthly visits based on user base
            # Assumption: Active users visit 10x per month
            estimated_visits = comp['users_estimate'] * 10
            
            # Add some realistic variation
            for month in range(12):
                date = datetime(2025, month + 1, 1)
                
                # Growth trend (companies growing at different rates)
                if key == 'notion_ai':
                    growth_rate = 1.05  # 5% monthly
                elif key in ['mem_ai', 'recall']:
                    growth_rate = 1.15  # 15% monthly (rapid growth)
                else:
                    growth_rate = 1.08  # 8% monthly
                
                monthly_visits = int(estimated_visits * (growth_rate ** month))
                
                traffic_data.append({
                    'competitor_id': key,
                    'competitor_name': comp['name'],
                    'month': date,
                    'estimated_visits': monthly_visits,
                    'bounce_rate': np.random.uniform(0.35, 0.55),
                    'pages_per_visit': np.random.uniform(3.5, 6.5),
                    'avg_visit_duration_sec': np.random.uniform(180, 420)
                })
        
        self.traffic_data = pd.DataFrame(traffic_data)
        
        print(f"✅ Generated traffic data: 12 months × {len(COMPETITORS)} competitors")
        return self.traffic_data
    
    def generate_user_reviews(self) -> pd.DataFrame:
        """
        Generate synthetic user reviews (G2/Product Hunt style)
        """
        print("⭐ Generating user reviews...")
        
        reviews_data = []
        
        # Review templates by sentiment
        positive_reviews = [
            "Game-changer for my research workflow",
            "Finally found a tool that works the way I think",
            "Saves me hours every week organizing notes",
            "The AI summarization is incredibly accurate",
            "Love how it automatically links related concepts"
        ]
        
        neutral_reviews = [
            "Good tool but has a learning curve",
            "Works well for basic needs, missing some advanced features",
            "Solid option but expensive for what it offers",
            "Does what it says, nothing more",
            "Decent but not significantly better than alternatives"
        ]
        
        negative_reviews = [
            "Too complicated for my needs",
            "Buggy and crashes frequently",
            "Not worth the price",
            "Missing key features I need",
            "Customer support is slow to respond"
        ]
        
        for key, comp in COMPETITORS.items():
            # Generate 20 reviews per competitor
            n_reviews = 20
            
            # Rating distribution (most tools have 4.0-4.5 avg)
            # Notion AI: 4.5, Mem.ai: 4.3, Obsidian: 4.7, etc.
            rating_distributions = {
                'notion_ai': (4.5, 0.5),
                'mem_ai': (4.3, 0.6),
                'reflect': (4.4, 0.5),
                'obsidian': (4.7, 0.4),
                'roam': (4.0, 0.7),
                'napkin_ai': (4.2, 0.6),
                'recall': (4.4, 0.5)
            }
            
            mean_rating, std_rating = rating_distributions.get(key, (4.3, 0.5))
            
            for i in range(n_reviews):
                rating = np.clip(np.random.normal(mean_rating, std_rating), 1, 5)
                rating = round(rating * 2) / 2  # Round to 0.5
                
                # Select review text based on rating
                if rating >= 4.5:
                    review_text = np.random.choice(positive_reviews)
                    sentiment = 'positive'
                elif rating >= 3.5:
                    review_text = np.random.choice(neutral_reviews)
                    sentiment = 'neutral'
                else:
                    review_text = np.random.choice(negative_reviews)
                    sentiment = 'negative'
                
                reviews_data.append({
                    'competitor_id': key,
                    'competitor_name': comp['name'],
                    'rating': rating,
                    'review_text': review_text,
                    'sentiment': sentiment,
                    'date': datetime.now() - timedelta(days=np.random.randint(0, 365)),
                    'verified_purchase': np.random.choice([True, False], p=[0.7, 0.3]),
                    'helpful_count': np.random.poisson(5)
                })
        
        self.reviews_data = pd.DataFrame(reviews_data)
        
        print(f"✅ Generated {len(self.reviews_data)} user reviews")
        return self.reviews_data
    
    def save_all_data(self):
        """
        Save all generated data to CSV files
        """
        if self.competitors_df is not None:
            self.competitors_df.to_csv(PROCESSED_DATA_DIR / 'competitive_overview.csv', index=False)
            print(f"💾 Saved: competitive_overview.csv")
        
        if self.features_matrix is not None:
            self.features_matrix.to_csv(PROCESSED_DATA_DIR / 'feature_matrix.csv', index=False)
            print(f"💾 Saved: feature_matrix.csv")
        
        if self.traffic_data is not None:
            self.traffic_data.to_csv(SYNTHETIC_DATA_DIR / 'traffic_estimates.csv', index=False)
            print(f"💾 Saved: traffic_estimates.csv")
        
        if self.reviews_data is not None:
            self.reviews_data.to_csv(SYNTHETIC_DATA_DIR / 'user_reviews.csv', index=False)
            print(f"💾 Saved: user_reviews.csv")


if __name__ == "__main__":
    print("=" * 80)
    print(" COMPETITIVE DATA COLLECTOR")
    print("=" * 80)
    print()
    
    collector = CompetitiveDataCollector()
    
    # Generate all data
    collector.generate_competitive_overview()
    collector.generate_feature_matrix()
    collector.generate_traffic_estimates()
    collector.generate_user_reviews()
    
    # Save data
    collector.save_all_data()
    
    print("\n✅ All competitive data generated successfully!")
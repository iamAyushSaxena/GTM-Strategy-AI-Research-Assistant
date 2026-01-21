# System Architecture

## Overview
This document describes the technical architecture of the GTM Strategy Analysis system.

---

## Architecture Diagram
```
┌────────────────────────────────────────────────────────┐
│                     USER INTERFACE                     │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────────┐          ┌──────────────────┐   │
│   │  Streamlit App   │◄─────────┤ HTML Dashboards  │   │
│   │  (Interactive)   │          │ (Static Export)  │   │
│   └────────┬─────────┘          └──────────────────┘   │
│            │                                           │
└────────────┼───────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────┐
│                      ANALYSIS LAYER                    │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌──────────────┐  ┌─────────────┐  ┌───────────────┐  │
│  │ Competitive  │  │    Market   │  │    Pricing    │  │
│  │  Analyzer    │  │    Sizer    │  │   Strategy    │  │
│  └──────┬───────┘  └───────┬─────┘  └───────┬───────┘  │
│         │                  │                │          │
│  ┌──────┴───────┐  ┌───────┴─────┐  ┌───────┴───────┐  │
│  │     GTM      │  │  Financial  │  │ Visualization │  │
│  │   Planner    │  │    Model    │  │    Engine     │  │
│  └──────────────┘  └─────────────┘  └───────────────┘  │
│                                                        │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                       DATA LAYER                       │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌─────────────┐   ┌──────────────┐  ┌──────────────┐  │
│  │     Raw     │   │  Processed   │  │  Synthetic   │  │
│  │     Data    │   │     Data     │  │     Data     │  │
│  │   (Input)   │──►│ (Analysis)   │◄─│ (Generated)  │  │
│  └─────────────┘   └──────────────┘  └──────────────┘  │
│                                                        │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│                      OUTPUT LAYER                      │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Reports    │  │  Dashboards  │  │   Figures    │  │
│  │    (TXT)     │  │    (HTML)    │  │    (PNG)     │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## Component Details

### 1. Data Layer

#### **Data Collector (`data_collector.py`)**
**Purpose:** Generate synthetic competitive intelligence data

**Components:**
- `CompetitiveDataCollector` class
  - `generate_competitive_overview()`: Basic competitor info
  - `generate_feature_matrix()`: Feature scores (0-10 scale)
  - `generate_traffic_estimates()`: Monthly visit estimates
  - `generate_user_reviews()`: Synthetic reviews with sentiment

**Inputs:**
- Configuration from `config.py` (competitor list, features)

**Outputs:**
- `competitive_overview.csv`
- `feature_matrix.csv`
- `traffic_estimates.csv`
- `user_reviews.csv`

**Data Flow:**
```
config.py → CompetitiveDataCollector → CSV files → data/processed/
```

---

### 2. Analysis Layer

#### **Competitive Analyzer (`competitive_analyzer.py`)**
**Purpose:** Analyze competitive landscape and identify opportunities

**Components:**
- `CompetitiveAnalyzer` class
  - `calculate_positioning_coordinates()`: Map competitors on 2D grid
  - `identify_white_space()`: Find underserved quadrants
  - `perform_swot_analysis()`: SWOT for each competitor
  - `calculate_feature_gaps()`: Our product vs competitors

**Algorithm: Positioning Matrix**
```python
# Each competitor gets (x, y) coordinates
x = specialization_score (0=generalist, 10=specialist)
y = user_type_score (0=individual, 10=team)

# White space = quadrants with fewest competitors
quadrants = {
    'generalist_individual': count_competitors(x<5, y<5),
    'specialist_individual': count_competitors(x>=5, y<5),
    # ... etc
}
```

**Inputs:**
- `competitive_overview.csv`
- `feature_matrix.csv`

**Outputs:**
- `positioning_data.csv`
- `swot_analysis.csv`
- `feature_gaps.csv`
- `competitive_analysis_summary.txt`

---

#### **Market Sizer (`market_sizer.py`)**
**Purpose:** Calculate TAM/SAM/SOM with documented assumptions

**Components:**
- `MarketSizer` class
  - `calculate_tam()`: Total addressable market
  - `calculate_sam()`: Serviceable available market
  - `calculate_som()`: Serviceable obtainable market
  - `export_assumptions_table()`: Document all assumptions

**Algorithm: Market Sizing**
```python
# TAM: Bottom-up + Top-down validation
tam_bottomup = sum(all_segments)
tam_topdown = global_knowledge_workers * 0.25
tam_final = (tam_bottomup + tam_topdown) / 2

# SAM: Sequential filtering
sam = tam
sam *= 0.20  # English-language
sam *= 0.90  # Digital adoption
sam *= 0.70  # AI willingness
sam *= 0.60  # Payment willingness

# SOM: Beachhead market capture
som_potential = beachhead_segment * english_pct * active_pct
som_final = som_potential * awareness * signup * activation * market_share
```

**Inputs:**
- `config.py` (MARKET_SIZE constants)

**Outputs:**
- `market_sizing_assumptions.csv`
- `market_sizing_report.txt`

---

#### **Pricing Strategy (`pricing_strategy.py`)**
**Purpose:** Develop pricing and validate unit economics

**Components:**
- `PricingStrategy` class
  - `analyze_competitor_pricing()`: Benchmark analysis
  - `calculate_value_metrics()`: ROI and value delivered
  - `validate_unit_economics()`: LTV/CAC/payback calculations

**Algorithm: Unit Economics**
```python
# LTV Calculation
ltv = arpu * avg_lifetime_months * gross_margin
    = $15 * 24 * 0.70
    = $252

# CAC Calculation (blended)
cac = sum(channel_cac * channel_mix)
    = ($20*0.4) + ($15*0.3) + ($50*0.2) + ($10*0.1)
    = $35

# Health Metrics
ltv_cac_ratio = ltv / cac = 7.2x
payback_months = cac / (arpu * gross_margin) = 3.3 months
```

**Inputs:**
- `competitive_overview.csv`
- `config.py` (PRICING_TIERS, UNIT_ECONOMICS)

**Outputs:**
- `pricing_strategy_recommendation.txt`

---

#### **GTM Planner (`gtm_planner.py`)**
**Purpose:** Create 90-day launch roadmap

**Components:**
- `GTMPlanner` class
  - `create_weekly_breakdown()`: 12-week plan with tasks
  - `define_channel_strategy()`: 6 acquisition channels with CAC
  - `generate_gtm_report()`: Executive summary

**Data Structure: Weekly Plan**
```python
{
    'week': 1,
    'phase': 'Phase 1: Private Beta',
    'focus': 'Beta Recruitment',
    'tasks': ['Task 1', 'Task 2', ...],
    'metrics': {'signups': 30, 'activation_rate': 0.35},
    'budget': 500
}
```

**Inputs:**
- `config.py` (GTM_ROADMAP, SUCCESS_METRICS)

**Outputs:**
- `gtm_weekly_plan.csv`
- `gtm_strategy_report.txt`

---

#### **Financial Model (`financial_model.py`)**
**Purpose:** Project revenue and profitability

**Components:**
- `FinancialModel` class
  - `project_user_growth()`: 24-month user projections
  - `calculate_break_even()`: Profitability timeline
  - `generate_financial_report()`: Executive summary

**Algorithm: Growth Projections**
```python
for month in range(1, 25):
    # User acquisition
    organic_signups = base_signups * (growth_rate ** month)
    viral_signups = current_users * viral_coefficient
    total_new_users = organic_signups + viral_signups
    
    # Churn
    churned_users = current_users * churn_rate
    current_users += total_new_users - churned_users
    
    # Revenue
    new_paying = total_new_users * free_to_paid_rate
    churned_paying = current_paying * churn_rate * 0.5
    current_paying += new_paying - churned_paying
    mrr = current_paying * arpu
    
    # Costs
    cogs = current_users * 4.00  # API + infra
    opex = product_dev + sales_marketing + g_and_a
    net_profit = mrr - cogs - opex
```

**Inputs:**
- `config.py` (FINANCIAL_PROJECTIONS, SUCCESS_METRICS)

**Outputs:**
- `financial_projections_24m.csv`
- `financial_model_report.txt`

---

#### **Visualization Engine (`visualization.py`)**
**Purpose:** Create charts and dashboards

**Components:**
- `GTMVisualizer` class
  - `plot_positioning_matrix()`: Interactive scatter plot
  - `plot_feature_comparison()`: Radar chart
  - `plot_tam_sam_som_funnel()`: Funnel visualization
  - `plot_financial_projections()`: Multi-panel time series
  - `plot_channel_mix()`: Pie chart

**Technology Stack:**
- Plotly (interactive charts)
- Matplotlib (static exports)
- Seaborn (statistical viz)

**Inputs:**
- All CSV files from data/processed/

**Outputs:**
- HTML dashboards (outputs/dashboards/)
- PNG figures (outputs/figures/)

---

### 3. User Interface Layer

#### **Streamlit App (`streamlit_app.py`)**
**Purpose:** Interactive dashboard for presenting strategy

**Architecture:**
```python
# Page structure
pages = [
    "Executive Summary",      # Overview metrics
    "Market Opportunity",     # TAM/SAM/SOM
    "Competitive Analysis",   # Positioning, features
    "Pricing Strategy",       # Tiers, economics
    "90-Day GTM Plan",       # Roadmap, channels
    "Financial Projections", # 24-month model
    "Dashboard"              # Consolidated view
]

# Data loading (cached)
@st.cache_data
def load_data():
    return {
        'competitors': pd.read_csv(...),
        'features': pd.read_csv(...),
        'financial': pd.read_csv(...),
        # ...
    }

# Visualization integration
viz = GTMVisualizer()
fig = viz.plot_positioning_matrix(data)
st.plotly_chart(fig)
```

**Features:**
- 7 navigation pages
- Real-time filtering
- Interactive charts (zoom, pan, hover)
- Metric cards
- Downloadable reports

---

## Data Models

### **Competitor Data Model**
```python
{
    'competitor_id': str,           # Unique identifier
    'name': str,                    # Display name
    'description': str,             # Product description
    'founded_year': int,            # Year founded
    'ai_added_year': int,           # When AI was added
    'positioning': str,             # Market position
    'pricing': {                    # Pricing tiers
        'free': bool,
        'pro': float,
        'team': float
    },
    'users_estimate': int,          # Estimated users
    'total_funding_usd': int,       # Total funding
    'latest_valuation_usd': int     # Latest valuation
}
```

### **Feature Matrix Model**
```python
{
    'competitor_id': str,
    'feature': str,                 # Feature name
    'score': int                    # 0-10 scale
}
```

### **Financial Projection Model**
```python
{
    'month': int,                   # 1-24
    'date': str,                    # YYYY-MM
    'total_users': int,
    'paying_users': int,
    'mrr': float,
    'arr': float,
    'churn_rate': float,
    'ltv_cac_ratio': float,
    'net_profit': float
}
```

---

## Configuration Management

### **config.py Structure**
```python
# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
# ...

# Product definition
PRODUCT_NAME = "ResearchFlow AI"
PRODUCT_TAGLINE = "..."
PRODUCT_DESCRIPTION = "..."

# Target market
TARGET_MARKET = {...}

# Market sizing
MARKET_SIZE = {
    'tam': {...},
    'sam': {...},
    'som': {...}
}

# Competitors (7 major)
COMPETITORS = {
    'notion_ai': {...},
    'mem_ai': {...},
    # ...
}

# Features (15 dimensions)
FEATURE_DIMENSIONS = [...]

# Pricing tiers
PRICING_TIERS = {...}

# Unit economics
UNIT_ECONOMICS = {...}

# GTM roadmap
GTM_ROADMAP = {...}

# Success metrics
SUCCESS_METRICS = {...}
```

---

## Execution Flow

### **Full Analysis Pipeline**
```
1. scripts/run_full_analysis.py
   ├─ Import all modules
   ├─ Step 1: Data Collection
   │  └─ CompetitiveDataCollector.generate_all()
   │     └─ Save to data/processed/
   │
   ├─ Step 2: Competitive Analysis
   │  └─ CompetitiveAnalyzer.analyze()
   │     └─ Save positioning, SWOT, gaps
   │
   ├─ Step 3: Market Sizing
   │  └─ MarketSizer.calculate_all()
   │     └─ Save TAM/SAM/SOM report
   │
   ├─ Step 4: Pricing Strategy
   │  └─ PricingStrategy.validate()
   │     └─ Save pricing recommendation
   │
   ├─ Step 5: GTM Planning
   │  └─ GTMPlanner.create_plan()
   │     └─ Save weekly roadmap
   │
   ├─ Step 6: Financial Modeling
   │  └─ FinancialModel.project()
   │     └─ Save 24-month projections
   │
   └─ Step 7: Visualizations
      └─ GTMVisualizer.generate_all()
         └─ Save HTML dashboards
```

### **Streamlit App Launch**
```
streamlit run app/streamlit_app.py
   ├─ Load cached data
   ├─ Initialize GTMVisualizer
   ├─ Render sidebar navigation
   ├─ Display selected page
   │  ├─ Executive Summary
   │  ├─ Market Opportunity
   │  ├─ Competitive Analysis
   │  ├─ Pricing Strategy
   │  ├─ 90-Day GTM Plan
   │  ├─ Financial Projections
   │  └─ Dashboard
   └─ Handle user interactions
```

---

## Technology Stack

### **Core**
- Python 3.13+
- pandas 2.1.3 (data manipulation)
- numpy 1.24.3 (numerical computing)

### **Visualization**
- plotly 5.18.0 (interactive charts)
- matplotlib 3.8.2 (static charts)
- seaborn 0.13.0 (statistical viz)

### **Web Framework**
- streamlit 1.29.0 (dashboard)
- streamlit-option-menu 0.3.6 (navigation)

### **Document Generation**
- fpdf 1.7.2 (PDF export)
- markdown 3.5 (Markdown processing)

### **Development**
- jupyter 1.0.0 (notebooks)
- pytest 7.4.3 (testing)
- black 23.12.1 (code formatting)

---

## Performance Characteristics

### **Execution Time**
- Full analysis pipeline: ~30 seconds
- Data generation: ~5 seconds
- Analysis calculations: ~10 seconds
- Visualization generation: ~15 seconds

### **Memory Usage**
- Peak memory: ~200 MB
- Data files: ~5 MB total
- Dashboard runtime: ~100 MB

### **Scalability**
- Current: 7 competitors, 24 months, single market
- Can scale to: 50+ competitors, 60+ months, multiple markets
- Bottleneck: Visualization rendering (acceptable at current scale)

---

## Error Handling

### **Data Validation**
```python
# Example from market_sizer.py
if tam_final <= 0:
    raise ValueError("TAM must be positive")

if sam > tam:
    raise ValueError("SAM cannot exceed TAM")

if som > sam:
    raise ValueError("SOM cannot exceed SAM")
```

### **File I/O**
```python
# Example from data_collector.py
try:
    df.to_csv(output_path, index=False)
    print(f"✅ Saved: {output_path.name}")
except IOError as e:
    print(f"❌ Failed to save {output_path.name}: {e}")
```

### **User Input**
```python
# Example from streamlit_app.py
try:
    data = load_data()
except FileNotFoundError:
    st.error("⚠️ Data files not found. Please run analysis first.")
    st.stop()
```

---

## Testing Strategy

### **Unit Tests**
```python
# tests/test_market_sizer.py
def test_tam_calculation():
    sizer = MarketSizer()
    tam = sizer.calculate_tam()
    assert tam['final'] > 0
    assert tam['final'] == 300_000_000

def test_sam_filtering():
    sizer = MarketSizer()
    sizer.calculate_tam()
    sam = sizer.calculate_sam()
    assert sam['final'] < sizer.tam_data['final']
```

### **Integration Tests**
```python
# tests/test_full_pipeline.py
def test_end_to_end():
    # Run full analysis
    subprocess.run(['python', 'scripts/run_full_analysis.py'])
    
    # Check outputs exist
    assert (PROCESSED_DATA_DIR / 'competitive_overview.csv').exists()
    assert (REPORTS_DIR / 'market_sizing_report.txt').exists()
```

---

## Security Considerations

### **Data Privacy**
- All data is synthetic (no real user data)
- No API keys or credentials stored
- No external API calls (self-contained)

### **Code Security**
- No eval() or exec() usage
- Path traversal protection (using pathlib)
- Input validation on all user inputs

---

## Future Enhancements

### **Planned Features**
1. **Real Data Integration**
   - Crunchbase API for funding data
   - SimilarWeb API for traffic estimates
   - Web scraping (with rate limiting)

2. **Advanced Analytics**
   - Monte Carlo simulation for sensitivity analysis
   - Cohort retention predictions (ML model)
   - Competitive moat scoring algorithm

3. **Export Capabilities**
   - PDF report generation
   - PowerPoint deck export
   - CSV data exports with metadata

4. **Collaboration**
   - Multi-user scenarios (bull/base/bear)
   - Version control for assumptions
   - Comment system for strategy review

---

## Maintenance

### **Updating Dependencies**
```bash
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt
```

### **Data Refresh**
```bash
# Re-generate all data
python scripts/collect_data.py

# Re-run analysis
python scripts/run_full_analysis.py
```

### **Code Quality**
```bash
# Format code
black src/ app/ scripts/

# Run tests
pytest tests/ -v

# Check coverage
pytest --cov=src tests/
```

---

*Architecture Version: 1.0*
*Author: Ayush Saxena*
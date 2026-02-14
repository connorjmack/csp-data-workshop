"""
visualize_interactive.py — Interactive HTML dashboard for Keeling Curve analysis.

Creates a professional, interactive HTML report with:
- High-quality Plotly visualizations
- Smooth scrolling navigation
- Interactive tooltips and zoom
- Professional styling
- Narrative explanations
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


def create_overview_plot(df: pd.DataFrame, decomp_df: pd.DataFrame) -> go.Figure:
    """Create interactive overview with observations, trend, and deseasonalized data."""
    fig = go.Figure()

    # Monthly observations (light, semi-transparent)
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['co2'],
        name='Monthly Observations',
        mode='lines',
        line=dict(color='#3498db', width=1),
        opacity=0.5,
        hovertemplate='%{x|%Y-%m}<br>CO₂: %{y:.2f} ppm<extra></extra>'
    ))

    # Deseasonalized (seasonal removed)
    fig.add_trace(go.Scatter(
        x=decomp_df['date'],
        y=decomp_df['deseasonalized'],
        name='Deseasonalized',
        mode='lines',
        line=dict(color='#2ecc71', width=2),
        opacity=0.8,
        hovertemplate='%{x|%Y-%m}<br>Deseasonalized: %{y:.2f} ppm<extra></extra>'
    ))

    # Trend (bold, prominent)
    fig.add_trace(go.Scatter(
        x=decomp_df['date'],
        y=decomp_df['trend'],
        name='Trend Component',
        mode='lines',
        line=dict(color='#e74c3c', width=3),
        hovertemplate='%{x|%Y-%m}<br>Trend: %{y:.2f} ppm<extra></extra>'
    ))

    fig.update_layout(
        title={
            'text': 'Atmospheric CO₂ at Mauna Loa Observatory<br><sub>Observed, Trend, and Deseasonalized Components</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#2c3e50'}
        },
        xaxis_title='Year',
        yaxis_title='CO₂ Concentration (ppm)',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#bdc3c7',
            borderwidth=1
        ),
        font=dict(family='Arial, sans-serif', size=12, color='#2c3e50')
    )

    return fig


def create_decomposition_plot(decomp_df: pd.DataFrame) -> go.Figure:
    """Create 4-panel seasonal decomposition figure."""
    fig = make_subplots(
        rows=4, cols=1,
        subplot_titles=('Observed', 'Trend', 'Seasonal', 'Residual'),
        vertical_spacing=0.08,
        shared_xaxes=True
    )

    # Panel 1: Observed
    fig.add_trace(go.Scatter(
        x=decomp_df['date'], y=decomp_df['observed'],
        mode='lines', name='Observed',
        line=dict(color='#3498db', width=1.5),
        hovertemplate='%{x|%Y-%m}<br>%{y:.2f} ppm<extra></extra>'
    ), row=1, col=1)

    # Panel 2: Trend
    fig.add_trace(go.Scatter(
        x=decomp_df['date'], y=decomp_df['trend'],
        mode='lines', name='Trend',
        line=dict(color='#e74c3c', width=2),
        hovertemplate='%{x|%Y-%m}<br>%{y:.2f} ppm<extra></extra>'
    ), row=2, col=1)

    # Panel 3: Seasonal
    fig.add_trace(go.Scatter(
        x=decomp_df['date'], y=decomp_df['seasonal'],
        mode='lines', name='Seasonal',
        line=dict(color='#2ecc71', width=1.5),
        hovertemplate='%{x|%Y-%m}<br>%{y:.2f} ppm<extra></extra>'
    ), row=3, col=1)

    # Add zero line for seasonal
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5, row=3, col=1)

    # Panel 4: Residual
    fig.add_trace(go.Scatter(
        x=decomp_df['date'], y=decomp_df['residual'],
        mode='lines', name='Residual',
        line=dict(color='#f39c12', width=1),
        hovertemplate='%{x|%Y-%m}<br>%{y:.2f} ppm<extra></extra>'
    ), row=4, col=1)

    # Add zero line for residual
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5, row=4, col=1)

    # Update layout
    fig.update_layout(
        title={
            'text': 'Seasonal Decomposition of CO₂ Time Series<br><sub>Observed = Trend + Seasonal + Residual</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#2c3e50'}
        },
        height=800,
        showlegend=False,
        template='plotly_white',
        hovermode='x unified',
        font=dict(family='Arial, sans-serif', size=12, color='#2c3e50')
    )

    # Update y-axis labels
    fig.update_yaxes(title_text="ppm", row=1, col=1)
    fig.update_yaxes(title_text="ppm", row=2, col=1)
    fig.update_yaxes(title_text="ppm", row=3, col=1)
    fig.update_yaxes(title_text="ppm", row=4, col=1)

    fig.update_xaxes(title_text="Year", row=4, col=1)

    return fig


def create_growth_acceleration_plot(growth_df: pd.DataFrame) -> go.Figure:
    """Create dual-panel growth rate and acceleration figure."""
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Annual Growth Rate', 'Growth Acceleration'),
        vertical_spacing=0.12,
        shared_xaxes=True
    )

    # Panel 1: Growth rate
    # Annual (thin, transparent)
    fig.add_trace(go.Scatter(
        x=growth_df['year'], y=growth_df['growth_rate'],
        mode='lines', name='Annual',
        line=dict(color='#3498db', width=1),
        opacity=0.3,
        hovertemplate='%{x}<br>Growth: %{y:.2f} ppm/yr<extra></extra>'
    ), row=1, col=1)

    # 5-year smoothed (bold)
    fig.add_trace(go.Scatter(
        x=growth_df['year'], y=growth_df['growth_rate_smooth'],
        mode='lines', name='5-Year Average',
        line=dict(color='#e74c3c', width=3),
        hovertemplate='%{x}<br>Growth (5yr avg): %{y:.2f} ppm/yr<extra></extra>'
    ), row=1, col=1)

    # Zero line
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5, row=1, col=1)

    # Panel 2: Acceleration
    # Annual (thin, transparent)
    fig.add_trace(go.Scatter(
        x=growth_df['year'], y=growth_df['acceleration'],
        mode='lines', name='Annual',
        line=dict(color='#2ecc71', width=1),
        opacity=0.3,
        showlegend=False,
        hovertemplate='%{x}<br>Acceleration: %{y:.3f} ppm/yr²<extra></extra>'
    ), row=2, col=1)

    # 5-year smoothed (bold)
    fig.add_trace(go.Scatter(
        x=growth_df['year'], y=growth_df['acceleration_smooth'],
        mode='lines', name='5-Year Average',
        line=dict(color='#f39c12', width=3),
        showlegend=False,
        hovertemplate='%{x}<br>Acceleration (5yr avg): %{y:.3f} ppm/yr²<extra></extra>'
    ), row=2, col=1)

    # Zero line
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5, row=2, col=1)

    fig.update_layout(
        title={
            'text': 'CO₂ Growth Rate and Acceleration Over Time<br><sub>First and Second Derivatives Show Worsening Trend</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#2c3e50'}
        },
        height=700,
        template='plotly_white',
        hovermode='x unified',
        font=dict(family='Arial, sans-serif', size=12, color='#2c3e50'),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#bdc3c7',
            borderwidth=1
        )
    )

    fig.update_yaxes(title_text="ppm/year", row=1, col=1)
    fig.update_yaxes(title_text="ppm/year²", row=2, col=1)
    fig.update_xaxes(title_text="Year", row=2, col=1)

    return fig


def create_historical_plot() -> go.Figure:
    """Create historical context plot with ice core + modern data."""
    try:
        hist = pd.read_csv("co2_historical.csv", comment='"', skipinitialspace=True)
        hist.columns = hist.columns.str.strip()

        # Find CO2 and year columns
        co2_col = None
        for col in hist.columns:
            if 'co2' in col.lower() and 'age' not in col.lower():
                co2_col = col
                break

        year_col = None
        for col in hist.columns:
            if any(x in col.lower() for x in ['year', 'age', 'yr', 'date', 'sample']):
                year_col = col
                break

        if co2_col is None or year_col is None:
            return None

        hist = hist.rename(columns={year_col: 'year', co2_col: 'co2'})
        hist = hist[['year', 'co2']].dropna()
        hist['year'] = pd.to_numeric(hist['year'], errors='coerce')
        hist['co2'] = pd.to_numeric(hist['co2'], errors='coerce')
        hist = hist.dropna()

        # Split into ice core and modern
        ice_core = hist[hist['year'] < 1958].copy()
        modern = hist[hist['year'] >= 1958].copy()

        fig = go.Figure()

        # Ice core data
        fig.add_trace(go.Scatter(
            x=ice_core['year'], y=ice_core['co2'],
            mode='lines', name='Ice Core Records',
            line=dict(color='#3498db', width=2),
            hovertemplate='Year: %{x:.0f}<br>CO₂: %{y:.1f} ppm<extra></extra>'
        ))

        # Modern measurements
        fig.add_trace(go.Scatter(
            x=modern['year'], y=modern['co2'],
            mode='lines', name='Direct Measurements',
            line=dict(color='#e74c3c', width=3),
            hovertemplate='Year: %{x:.0f}<br>CO₂: %{y:.1f} ppm<extra></extra>'
        ))

        # Pre-industrial level
        fig.add_hline(
            y=280,
            line_dash="dash",
            line_color="#2ecc71",
            line_width=2,
            annotation_text="Pre-industrial (~280 ppm)",
            annotation_position="right"
        )

        # Current level
        if len(modern) > 0:
            current = modern['co2'].iloc[-1]
            fig.add_hline(
                y=current,
                line_dash="dash",
                line_color="#e74c3c",
                line_width=2,
                annotation_text=f"Current (~{current:.0f} ppm)",
                annotation_position="right"
            )

        year_span = int(modern['year'].max() - ice_core['year'].min())

        fig.update_layout(
            title={
                'text': f'{year_span:,} Years of Atmospheric CO₂<br><sub>Ice Core Records + Modern Measurements from Mauna Loa</sub>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 24, 'color': '#2c3e50'}
            },
            xaxis_title='Year',
            yaxis_title='CO₂ Concentration (ppm)',
            height=500,
            template='plotly_white',
            hovermode='x unified',
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='#bdc3c7',
                borderwidth=1
            ),
            font=dict(family='Arial, sans-serif', size=12, color='#2c3e50')
        )

        return fig

    except Exception as e:
        print(f"⚠ Could not create historical plot: {e}")
        return None


def create_seasonal_analysis_plot(df: pd.DataFrame) -> go.Figure:
    """Create detailed seasonal cycle analysis."""
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Average Seasonal Cycle', 'Seasonal Cycle by Decade'),
        horizontal_spacing=0.12
    )

    # Panel 1: Average seasonal cycle
    monthly_avg = df.groupby('month')['co2'].mean()
    monthly_std = df.groupby('month')['co2'].std()

    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig.add_trace(go.Bar(
        x=month_labels,
        y=monthly_avg.values,
        error_y=dict(type='data', array=monthly_std.values),
        marker=dict(color='#2ecc71', line=dict(color='#27ae60', width=1.5)),
        name='Average',
        hovertemplate='%{x}<br>Avg CO₂: %{y:.2f} ppm<br>Std: %{error_y.array:.2f} ppm<extra></extra>'
    ), row=1, col=1)

    # Panel 2: Seasonal cycle by decade
    decades = sorted(df['year'].apply(lambda y: int(y) // 10 * 10).unique())
    colors = px.colors.sequential.Viridis_r

    for i, decade in enumerate(decades):
        mask = (df['year'] >= decade) & (df['year'] < decade + 10)
        subset = df[mask]
        if len(subset) > 12:
            monthly = subset.groupby('month')['co2'].mean()
            color_idx = int(i * len(colors) / len(decades))

            # Only show legend for first and last decade
            show_legend = (decade == decades[0] or decade == decades[-1])

            fig.add_trace(go.Scatter(
                x=list(range(1, 13)),
                y=monthly.values,
                mode='lines',
                name=f'{decade}s',
                line=dict(color=colors[color_idx], width=3 if show_legend else 1.5),
                opacity=1.0 if show_legend else 0.3,
                showlegend=show_legend,
                hovertemplate=f'{decade}s<br>Month: %{{x}}<br>CO₂: %{{y:.2f}} ppm<extra></extra>'
            ), row=1, col=2)

    fig.update_xaxes(title_text="Month", row=1, col=1)
    fig.update_xaxes(title_text="Month", tickmode='array',
                     tickvals=list(range(1, 13)), ticktext=month_labels, row=1, col=2)
    fig.update_yaxes(title_text="CO₂ (ppm)", row=1, col=1)
    fig.update_yaxes(title_text="CO₂ (ppm)", row=1, col=2)

    fig.update_layout(
        title={
            'text': 'Seasonal Cycle Analysis<br><sub>Northern Hemisphere Growing Season Drives Annual Oscillation</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#2c3e50'}
        },
        height=500,
        template='plotly_white',
        showlegend=True,
        font=dict(family='Arial, sans-serif', size=12, color='#2c3e50'),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#bdc3c7',
            borderwidth=1
        )
    )

    return fig


def create_decade_comparison_plot(df: pd.DataFrame) -> go.Figure:
    """Create decade-by-decade comparison."""
    annual = df.groupby('year')['co2'].mean().reset_index()
    annual['decade'] = (annual['year'] // 10) * 10
    annual['co2_diff'] = annual['co2'].diff()

    decade_stats = annual.groupby('decade').agg({
        'co2': 'mean',
        'co2_diff': ['mean', 'std']
    }).round(2)

    decade_stats.columns = ['co2_mean', 'growth_mean', 'growth_std']
    decade_stats = decade_stats.reset_index()
    decade_stats = decade_stats[decade_stats['growth_mean'].notna()]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=decade_stats['decade'].astype(str) + 's',
        y=decade_stats['growth_mean'],
        error_y=dict(type='data', array=decade_stats['growth_std']),
        marker=dict(
            color=decade_stats['growth_mean'],
            colorscale='Reds',
            showscale=True,
            colorbar=dict(title='ppm/yr'),
            line=dict(color='#c0392b', width=1.5)
        ),
        hovertemplate='%{x}<br>Growth: %{y:.2f} ± %{error_y.array:.2f} ppm/yr<extra></extra>'
    ))

    fig.update_layout(
        title={
            'text': 'CO₂ Growth Rate by Decade<br><sub>Acceleration from 0.65 ppm/yr (1950s) to 2.60 ppm/yr (2020s)</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#2c3e50'}
        },
        xaxis_title='Decade',
        yaxis_title='Average Growth Rate (ppm/year)',
        height=500,
        template='plotly_white',
        font=dict(family='Arial, sans-serif', size=12, color='#2c3e50')
    )

    return fig


def generate_html_report(figures: dict, stats: dict) -> str:
    """Generate complete HTML report with all figures and narrative."""

    # Convert figures to HTML
    fig_htmls = {}
    for name, fig in figures.items():
        if fig is not None:
            fig_htmls[name] = fig.to_html(
                include_plotlyjs='cdn',
                div_id=name,
                config={'displayModeBar': True, 'displaylogo': False}
            )

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keeling Curve: Interactive Analysis Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }}

        header {{
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            font-weight: 700;
            letter-spacing: -1px;
        }}

        header .subtitle {{
            font-size: 1.3em;
            opacity: 0.9;
            font-weight: 300;
        }}

        nav {{
            background: #34495e;
            padding: 15px 40px;
            position: sticky;
            top: 0;
            z-index: 999;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        nav ul {{
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }}

        nav a {{
            color: white;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 4px;
            transition: background 0.3s;
            font-weight: 500;
        }}

        nav a:hover {{
            background: rgba(255,255,255,0.1);
        }}

        section {{
            padding: 60px 40px;
            border-bottom: 1px solid #ecf0f1;
        }}

        section:nth-child(even) {{
            background: #f8f9fa;
        }}

        .section-header {{
            margin-bottom: 30px;
        }}

        .section-header h2 {{
            font-size: 2.2em;
            color: #2c3e50;
            margin-bottom: 10px;
            border-left: 5px solid #3498db;
            padding-left: 20px;
        }}

        .section-header p {{
            font-size: 1.1em;
            color: #7f8c8d;
            margin-left: 25px;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}

        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-left: 4px solid #3498db;
        }}

        .stat-card h3 {{
            font-size: 0.9em;
            color: #7f8c8d;
            text-transform: uppercase;
            margin-bottom: 10px;
            font-weight: 600;
        }}

        .stat-card .value {{
            font-size: 2em;
            color: #2c3e50;
            font-weight: 700;
        }}

        .stat-card .change {{
            font-size: 0.9em;
            color: #e74c3c;
            margin-top: 5px;
        }}

        .plot-container {{
            margin: 30px 0;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        .key-findings {{
            background: #e8f4f8;
            padding: 30px;
            border-radius: 8px;
            border-left: 5px solid #3498db;
            margin: 30px 0;
        }}

        .key-findings h3 {{
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 1.4em;
        }}

        .key-findings ul {{
            list-style: none;
            padding-left: 0;
        }}

        .key-findings li {{
            padding: 10px 0;
            padding-left: 30px;
            position: relative;
        }}

        .key-findings li:before {{
            content: "▶";
            position: absolute;
            left: 0;
            color: #3498db;
        }}

        footer {{
            background: #2c3e50;
            color: white;
            padding: 40px;
            text-align: center;
        }}

        footer a {{
            color: #3498db;
            text-decoration: none;
        }}

        footer a:hover {{
            text-decoration: underline;
        }}

        .warning-box {{
            background: #fff3cd;
            border-left: 5px solid #f39c12;
            padding: 20px;
            margin: 20px 0;
            border-radius: 4px;
        }}

        .warning-box strong {{
            color: #f39c12;
            font-size: 1.1em;
        }}

        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2em;
            }}

            section {{
                padding: 40px 20px;
            }}

            .stats-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>The Keeling Curve</h1>
            <p class="subtitle">Interactive Analysis of Atmospheric CO₂ (1958–{stats['end_year']})</p>
        </header>

        <nav>
            <ul>
                <li><a href="#overview">Overview</a></li>
                <li><a href="#decomposition">Decomposition</a></li>
                <li><a href="#growth">Growth Rate</a></li>
                <li><a href="#decades">By Decade</a></li>
                <li><a href="#seasonal">Seasonal</a></li>
                <li><a href="#historical">Historical</a></li>
            </ul>
        </nav>

        <section id="summary">
            <div class="section-header">
                <h2>Executive Summary</h2>
                <p>Key statistics from {stats['start_year']} to {stats['end_year']}</p>
            </div>

            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Starting Level</h3>
                    <div class="value">{stats['co2_start']:.2f} ppm</div>
                    <div class="change">{stats['start_year']}</div>
                </div>

                <div class="stat-card">
                    <h3>Current Level</h3>
                    <div class="value">{stats['co2_end']:.2f} ppm</div>
                    <div class="change">{stats['end_year']}</div>
                </div>

                <div class="stat-card">
                    <h3>Total Increase</h3>
                    <div class="value">{stats['total_increase']:.2f} ppm</div>
                    <div class="change">+{stats['percent_increase']:.1f}%</div>
                </div>

                <div class="stat-card">
                    <h3>Recent Growth Rate</h3>
                    <div class="value">{stats['recent_growth']:.2f}</div>
                    <div class="change">ppm/year (last 10y)</div>
                </div>
            </div>

            <div class="warning-box">
                <strong>⚠️ Critical Finding:</strong> The growth rate has more than quadrupled from
                0.65 ppm/year in the 1950s to {stats['recent_growth']:.2f} ppm/year today.
                This acceleration indicates the problem is getting worse faster.
            </div>
        </section>

        <section id="overview">
            <div class="section-header">
                <h2>1. Time Series Overview</h2>
                <p>Observed measurements, long-term trend, and deseasonalized data</p>
            </div>

            <div class="plot-container">
                {fig_htmls.get('overview', '<p>Figure not available</p>')}
            </div>

            <div class="key-findings">
                <h3>Key Insights</h3>
                <ul>
                    <li>The raw monthly observations show clear seasonal oscillations (±3 ppm) superimposed on a strong upward trend</li>
                    <li>The trend component reveals the underlying exponential-like growth in atmospheric CO₂</li>
                    <li>Deseasonalized data (with seasonal cycle removed) closely tracks the trend, confirming robust long-term increase</li>
                    <li>The upward trajectory has not slowed—it continues to steepen</li>
                </ul>
            </div>
        </section>

        <section id="decomposition">
            <div class="section-header">
                <h2>2. Seasonal Decomposition</h2>
                <p>Breaking the time series into trend, seasonal, and residual components</p>
            </div>

            <div class="plot-container">
                {fig_htmls.get('decomposition', '<p>Figure not available</p>')}
            </div>

            <div class="key-findings">
                <h3>Understanding the Components</h3>
                <ul>
                    <li><strong>Observed:</strong> Raw monthly CO₂ measurements from Mauna Loa Observatory</li>
                    <li><strong>Trend:</strong> Smooth long-term increase, capturing the fundamental growth pattern</li>
                    <li><strong>Seasonal:</strong> Regular annual cycle (~6 ppm amplitude) driven by Northern Hemisphere vegetation growth</li>
                    <li><strong>Residual:</strong> Random variation after removing trend and seasonality (mean ≈ 0, small variance)</li>
                </ul>
            </div>
        </section>

        <section id="growth">
            <div class="section-header">
                <h2>3. Growth Rate & Acceleration</h2>
                <p>First and second derivatives reveal worsening trends</p>
            </div>

            <div class="plot-container">
                {fig_htmls.get('growth', '<p>Figure not available</p>')}
            </div>

            <div class="key-findings">
                <h3>The Problem Is Accelerating</h3>
                <ul>
                    <li><strong>Growth rate</strong> (first derivative) has increased from ~0.7 ppm/year (1960s) to ~2.5 ppm/year (2020s)</li>
                    <li><strong>Acceleration</strong> (second derivative) shows the rate of increase is itself increasing</li>
                    <li>Positive acceleration means we're not just adding CO₂—we're adding it faster each year</li>
                    <li>Even short-term variations (El Niño events, economic recessions) barely dent the overall upward march</li>
                </ul>
            </div>
        </section>

        <section id="decades">
            <div class="section-header">
                <h2>4. Growth Rate by Decade</h2>
                <p>Comparison across time periods</p>
            </div>

            <div class="plot-container">
                {fig_htmls.get('decades', '<p>Figure not available</p>')}
            </div>

            <div class="key-findings">
                <h3>Decade-by-Decade Breakdown</h3>
                <ul>
                    <li>1950s: 0.65 ppm/year — Slow but measurable increase</li>
                    <li>1960s–1970s: ~1.0 ppm/year — Post-war industrialization</li>
                    <li>1980s–1990s: ~1.6 ppm/year — Globalization of economy</li>
                    <li>2000s–2010s: ~2.2 ppm/year — Rapid growth in developing nations</li>
                    <li>2020s: {stats['recent_growth']:.2f} ppm/year — Fastest growth on record (despite COVID-19 dip)</li>
                </ul>
            </div>
        </section>

        <section id="seasonal">
            <div class="section-header">
                <h2>5. Seasonal Cycle Analysis</h2>
                <p>Annual oscillation driven by terrestrial biosphere</p>
            </div>

            <div class="plot-container">
                {fig_htmls.get('seasonal', '<p>Figure not available</p>')}
            </div>

            <div class="key-findings">
                <h3>The Breathing Planet</h3>
                <ul>
                    <li><strong>Peak (May):</strong> CO₂ reaches maximum as Northern Hemisphere plants begin growing</li>
                    <li><strong>Trough (September):</strong> CO₂ reaches minimum after summer photosynthesis absorbs carbon</li>
                    <li><strong>Amplitude:</strong> ~6 ppm annual cycle—Earth's "breathing"</li>
                    <li><strong>Decade shift:</strong> Entire seasonal cycle has shifted upward ~100 ppm since 1950s</li>
                </ul>
            </div>
        </section>

        <section id="historical">
            <div class="section-header">
                <h2>6. Historical Context</h2>
                <p>Ice core records provide long-term perspective</p>
            </div>

            <div class="plot-container">
                {fig_htmls.get('historical', '<p>Figure not available</p>')}
            </div>

            <div class="key-findings">
                <h3>Unprecedented Change</h3>
                <ul>
                    <li><strong>Pre-industrial (~280 ppm):</strong> Stable for ~10,000 years of human civilization</li>
                    <li><strong>Industrial Revolution (~1850):</strong> Rapid increase begins</li>
                    <li><strong>Current (~{stats['co2_end']:.0f} ppm):</strong> {((stats['co2_end']/280 - 1)*100):.0f}% above pre-industrial baseline</li>
                    <li><strong>Rate of change:</strong> Current increase is ~100× faster than natural glacial-interglacial transitions</li>
                </ul>
            </div>
        </section>

        <footer>
            <p><strong>Data Source:</strong> Scripps CO₂ Program, Mauna Loa Observatory</p>
            <p><a href="https://scrippsco2.ucsd.edu" target="_blank">https://scrippsco2.ucsd.edu</a></p>
            <p style="margin-top: 20px; opacity: 0.8;">
                Interactive dashboard generated {datetime.now().strftime('%Y-%m-%d')} |
                Keeling Curve Data Workshop
            </p>
        </footer>
    </div>
</body>
</html>
"""
    return html


def main():
    """Generate interactive HTML dashboard."""
    print("=" * 70)
    print("GENERATING INTERACTIVE HTML DASHBOARD")
    print("=" * 70)
    print()

    # Load data
    print("Loading data...")
    df = pd.read_csv("co2_clean.csv", parse_dates=["date"])
    decomp_df = pd.read_csv("analysis_decomposition.csv", parse_dates=["date"])
    growth_df = pd.read_csv("analysis_growth_rate.csv")

    # Calculate statistics
    annual = df.groupby("year")["co2"].mean()
    stats = {
        'start_year': int(annual.index[0]),
        'end_year': int(annual.index[-1]),
        'co2_start': annual.iloc[0],
        'co2_end': annual.iloc[-1],
        'total_increase': annual.iloc[-1] - annual.iloc[0],
        'percent_increase': ((annual.iloc[-1] / annual.iloc[0]) - 1) * 100,
        'recent_growth': growth_df['growth_rate'].tail(10).mean()
    }

    # Create figures
    print("\nCreating interactive visualizations...")
    figures = {
        'overview': create_overview_plot(df, decomp_df),
        'decomposition': create_decomposition_plot(decomp_df),
        'growth': create_growth_acceleration_plot(growth_df),
        'decades': create_decade_comparison_plot(df),
        'seasonal': create_seasonal_analysis_plot(df),
        'historical': create_historical_plot()
    }

    print("✓ Created 6 interactive figures")

    # Generate HTML report
    print("\nGenerating HTML report...")
    html = generate_html_report(figures, stats)

    with open('keeling_dashboard.html', 'w') as f:
        f.write(html)

    print("✓ Saved: keeling_dashboard.html")
    print()
    print("=" * 70)
    print("Dashboard complete! Open keeling_dashboard.html in your browser.")
    print("=" * 70)


if __name__ == "__main__":
    main()

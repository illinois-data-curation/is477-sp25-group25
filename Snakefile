rule all:
    input:
        "results/merged.csv",
        "results/merged_profile.csv",

        "results/cleaned_data.csv",
        "results/descriptive_stats.csv",
        "results/correlation_matrix.png",
        "results/arrest_rate_trend.png",
        "results/unemployment_rate_trend.png"

rule fetch:
    output:
        fbi="data/fbi.csv",
        census="data/census.csv"
    script:
        "scripts/fetch_fbi_data.py"

rule merge:
    input:
        fbi="data/fbi.csv",
        census="data/census.csv"
    output:
        "results/merged.csv"
    script:
        "scripts/merge_data.py"

rule profile:
    input:
        "results/merged.csv"
    output:
        temp("results/profile.csv")
    script:
        "scripts/profile_data.py"

rule clean:
    input:
        "results/merged.csv"
    output:
        "results/cleaned_data.csv"
    script:
        "scripts/clean_data.py"

rule analyze:
    input:
        "results/cleaned_data.csv"
    output:
        "results/descriptive_stats.csv",
        "results/correlation_matrix.png",
        "results/arrest_rate_trend.png",
        "results/unemployment_rate_trend.png"
    script:
        "scripts/analyze_data.py"
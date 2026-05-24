"""Report generation module"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import Dict, Any
import json


class Reporter:
    """Generate human-readable reports from scan results"""
    
    def __init__(self):
        self.console = Console()
    
    def print_summary(self, results: Dict[str, Any]):
        """Print a summary of scan results to console"""
        self.console.print("\n[bold cyan]🔍 Static Analysis Report[/bold cyan]\n")
        
        # Security issues
        security = results.get("security", {})
        if "results" in security:
            issues = len(security["results"])
            severity_high = sum(1 for r in security["results"] if r.get("issue_severity") == "HIGH")
            self.console.print(Panel(
                f"[red]Security Issues: {issues}[/red]\n"
                f"[bold red]High Severity: {severity_high}[/bold red]",
                title="🔒 Security"
            ))
        
        # Code quality
        quality = results.get("quality", {})
        quality_issues = quality.get("issues", [])
        if quality_issues:
            errors = sum(1 for q in quality_issues if q.get("type") == "error")
            warnings = sum(1 for q in quality_issues if q.get("type") == "warning")
            self.console.print(Panel(
                f"[yellow]Errors: {errors}[/yellow]\n"
                f"[dim yellow]Warnings: {warnings}[/dim yellow]",
                title="✨ Code Quality"
            ))
        
        # Style issues
        style = results.get("style", [])
        style_count = len([s for s in style if s.strip()])
        self.console.print(Panel(
            f"[blue]Style Issues: {style_count}[/blue]",
            title="🎨 Code Style"
        ))
        
        # Complexity
        complexity = results.get("complexity", {})
        if complexity and not complexity.get("error"):
            high_complexity = sum(
                1 for file_data in complexity.values()
                for func in file_data
                if isinstance(func, dict) and func.get("complexity", 0) > 10
            )
            self.console.print(Panel(
                f"[magenta]High Complexity Functions: {high_complexity}[/magenta]",
                title="📊 Complexity"
            ))
    
    def save_json(self, results: Dict[str, Any], output_path: str):
        """Save results as JSON file"""
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        self.console.print(f"\n[green]✓[/green] Report saved to: {output_path}")

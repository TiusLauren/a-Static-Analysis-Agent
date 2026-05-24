#!/usr/bin/env python3
"""CLI interface for Static Analysis Agent"""
import click
from pathlib import Path
from .scanner import CodeScanner
from .reporter import Reporter


@click.command()
@click.argument('target', type=click.Path(exists=True))
@click.option('--output', '-o', help='Output JSON report path')
@click.option('--security-only', is_flag=True, help='Run security scan only')
@click.option('--quality-only', is_flag=True, help='Run quality scan only')
def main(target: str, output: str, security_only: bool, quality_only: bool):
    """
    Static Analysis Agent - Scan code for security, quality, and complexity issues.
    
    TARGET: Path to file or directory to analyze
    """
    click.echo(f"🚀 Starting analysis of: {target}\n")
    
    scanner = CodeScanner(target)
    reporter = Reporter()
    
    # Run appropriate scans
    if security_only:
        results = {"security": scanner.scan_security()}
    elif quality_only:
        results = {"quality": scanner.scan_quality()}
    else:
        results = scanner.run_full_scan()
    
    # Display results
    reporter.print_summary(results)
    
    # Save to file if requested
    if output:
        reporter.save_json(results, output)
    
    click.echo("\n✅ Analysis complete!")


if __name__ == '__main__':
    main()

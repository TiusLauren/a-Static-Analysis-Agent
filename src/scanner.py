"""Core scanner module for static analysis"""
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Any


class CodeScanner:
    """Main scanner class that orchestrates different analysis tools"""
    
    def __init__(self, target_path: str):
        self.target = Path(target_path)
        if not self.target.exists():
            raise FileNotFoundError(f"Target path not found: {target_path}")
    
    def scan_security(self) -> Dict[str, Any]:
        """Run Bandit security scanner"""
        try:
            result = subprocess.run(
                ["bandit", "-r", str(self.target), "-f", "json"],
                capture_output=True,
                text=True,
                timeout=60
            )
            return json.loads(result.stdout) if result.stdout else {}
        except Exception as e:
            return {"error": str(e)}
    
    def scan_quality(self) -> Dict[str, Any]:
        """Run Pylint code quality checker"""
        try:
            result = subprocess.run(
                ["pylint", str(self.target), "--output-format=json"],
                capture_output=True,
                text=True,
                timeout=60
            )
            data = json.loads(result.stdout) if result.stdout else []
            return {"issues": data} if isinstance(data, list) else data
        except Exception as e:
            return {"error": str(e)}
    
    def scan_style(self) -> List[str]:
        """Run Flake8 style checker"""
        try:
            result = subprocess.run(
                ["flake8", str(self.target)],
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.stdout.strip().split('\n') if result.stdout else []
        except Exception as e:
            return [f"Error: {str(e)}"]
    
    def scan_complexity(self) -> Dict[str, Any]:
        """Run Radon complexity analyzer"""
        try:
            result = subprocess.run(
                ["radon", "cc", str(self.target), "-j"],
                capture_output=True,
                text=True,
                timeout=60
            )
            return json.loads(result.stdout) if result.stdout else {}
        except Exception as e:
            return {"error": str(e)}
    
    def run_full_scan(self) -> Dict[str, Any]:
        """Execute all scanners and aggregate results"""
        return {
            "target": str(self.target),
            "security": self.scan_security(),
            "quality": self.scan_quality(),
            "style": self.scan_style(),
            "complexity": self.scan_complexity()
        }

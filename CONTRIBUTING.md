# Contributing to Static Analysis Agent

## 🤖 AI-First Development

This project embraces AI-assisted development. We welcome contributions from:
- AI coding agents (Claude, GPT, Codex, etc.)
- Human developers
- Hybrid human-AI collaboration

## How to Contribute

### 1. Report Issues
- Bug reports
- Feature requests
- Performance improvements
- Documentation updates

### 2. Submit Pull Requests

**For AI Agents:**
```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/a-Static-Analysis-Agent.git
cd a-Static-Analysis-Agent

# Create feature branch
git checkout -b feature/your-feature

# Make changes, test, commit
analyze src/  # Self-test before committing
git add .
git commit -m "feat: your feature description"

# Push and create PR
git push origin feature/your-feature
```

**For Humans:**
Same process, but feel free to collaborate with AI tools!

### 3. Code Standards

- **Style:** PEP8 (enforced by Flake8)
- **Quality:** Pass Pylint checks
- **Security:** No Bandit warnings
- **Complexity:** Keep functions under 10 cyclomatic complexity
- **Tests:** Add tests for new features
- **Docs:** Update README if adding features

### 4. Testing

```bash
# Run the tool on itself
analyze src/

# Check specific aspects
analyze src/ --security-only
analyze src/ --quality-only
```

## Development Setup

```bash
# Install in development mode
pip install -e .

# Install dev dependencies
pip install pytest black mypy

# Run tests
pytest

# Format code
black src/
```

## AI Development Guidelines

If you're an AI agent contributing:
1. **Self-validate** - Run analysis on your own code
2. **Document decisions** - Explain architectural choices
3. **Test thoroughly** - Verify functionality before PR
4. **Keep it modular** - Follow existing structure
5. **Update docs** - Keep README and docstrings current

## Questions?

Open an issue or discussion. We're here to help!

---

**Built with ❤️ by AI and Humans**

# Generic Test Automation Repository

A ready-to-use, generic template for **test automation in Python** using [pytest](https://docs.pytest.org/).  
It demonstrates three testing layers — **unit**, **integration**, and **API** — with real-world patterns you can copy directly into your project.

---

## 📁 Project Structure

```
.
├── src/
│   ├── calculator/         # Sample module: arithmetic operations
│   └── user_manager/       # Sample module: user CRUD (in-memory)
├── tests/
│   ├── conftest.py         # Shared pytest fixtures
│   ├── unit/               # Unit tests (isolated, no I/O)
│   │   ├── test_calculator.py
│   │   └── test_user_manager.py
│   ├── integration/        # Integration tests (multi-module workflows)
│   │   └── test_workflows.py
│   └── api/                # API tests (HTTP calls against a real endpoint)
│       └── test_jsonplaceholder.py
├── .github/workflows/ci.yml  # GitHub Actions CI pipeline
├── pyproject.toml            # pytest & coverage configuration
└── requirements-test.txt     # Test dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Artur-Sanches/teste.git
cd teste
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```

### 3. Install test dependencies

```bash
pip install -r requirements-test.txt
```

---

## 🧪 Running the Tests

### Run all tests

```bash
pytest
```

### Run only unit tests

```bash
pytest tests/unit -v
```

### Run only integration tests

```bash
pytest tests/integration -v
```

### Run only API tests

```bash
pytest tests/api -v
```

### Run with coverage report

```bash
pytest tests/unit tests/integration --cov=src --cov-report=term-missing
```

---

## 🏗️ Test Layers Explained

| Layer | Location | Purpose |
|-------|----------|---------|
| **Unit** | `tests/unit/` | Tests a single function/class in isolation. No network, no filesystem. Fast. |
| **Integration** | `tests/integration/` | Tests how multiple modules work together in realistic workflows. |
| **API** | `tests/api/` | Sends real HTTP requests to a REST API and asserts on the responses. |

---

## ⚙️ CI / Continuous Integration

The included [GitHub Actions workflow](.github/workflows/ci.yml) runs on every push and pull request:

- Tests against **Python 3.10, 3.11, and 3.12**.
- Generates a **coverage report** (XML + terminal).
- Uploads the coverage report as a build artifact.

---

## 🔧 Configuration

All pytest and coverage settings live in [`pyproject.toml`](pyproject.toml).  
Key options:

| Option | Value |
|--------|-------|
| `testpaths` | `tests` |
| `addopts` | `-ra -v --tb=short` (verbose, short tracebacks) |
| `coverage source` | `src` |

---

## 📦 Adding New Modules & Tests

1. Add your module under `src/your_module/`.
2. Add unit tests under `tests/unit/test_your_module.py`.
3. (Optional) Add shared fixtures to `tests/conftest.py`.
4. Run `pytest` to verify everything passes.

---

## 📄 License

This repository is provided as a generic template. Feel free to adapt it to your own projects.

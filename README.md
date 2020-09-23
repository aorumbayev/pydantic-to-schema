<p align="center">
    <a><img src="https://user-images.githubusercontent.com/7698600/94006948-ee21ab00-fda0-11ea-9542-719db825fbbd.png" height="250"/></a>
<br />
</p>

## About

Simple pre-commit hook to convert pydantic models to schemas

## Usage

Add this to your `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/aorumbayev/pydantic-to-schema
    rev: "" # can specify specific revision if needed
    hooks:
      - id: pydantic-to-schema
        args:
          [
            "--input",
            { path to module with models },
            "--output",
            { path to output folder },
          ]
```

### Params

- `--input` - param for a string relative path to a python module in your repository that contains the pydantic models. **IMPORTANT** make sure to import all `BaseModel` subclasses in `__init__.py` file.
- `--output` - param for a string relative path to a folder where you would like to dump exported `JSON Schemas`. Naming convention is as follows `{YourClassName}.json`. If folder already exists, it will recreate it and regenerate all schemas inside.

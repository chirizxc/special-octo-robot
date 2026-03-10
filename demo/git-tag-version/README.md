# git-tag-version demo

This folder is used by `.github/workflows/git-tag-version-demo.yml`.

On a tag push like `demo-1.2.3`, the workflow rewrites `demo/git-tag-version/Cargo.toml`
from:

```toml
version = "0.0.0"
```

to:

```toml
version = "demo-1.2.3"
```

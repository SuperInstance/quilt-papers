# quilt-papers

> **Canon that publishes.**
> Convert canon lore to academic paper format.

## TL;DR

```python
from quilt_papers import canon_to_paper, canon_to_bibtex

paper = canon_to_paper(
    title="The Substrate Walker Canon",
    lore="Long canon lore text...",
)
print(paper["abstract"])
print(paper["body"])

bibtex = canon_to_bibtex(paper["title"])
print(bibtex)
```

## License

MIT — Casey / SuperInstance, Sept 23, 2026

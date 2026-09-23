"""Convert canon lore to academic-paper format.

The Quilt canon is substrate-walker-aligned lore. This package converts
lore to academic-paper format (title, abstract, sections, references)
suitable for academic venues.
"""
from datetime import datetime


def canon_to_paper(
    title: str,
    lore: str,
    authors: list = None,
    abstract_chars: int = 500,
) -> dict:
    """Convert canon lore to a paper draft."""
    authors = authors or ["Casey Digennaro / SuperInstance"]
    
    # Extract first paragraph as abstract
    paragraphs = [p.strip() for p in lore.split("\n\n") if p.strip()]
    abstract = paragraphs[0][:abstract_chars] if paragraphs else lore[:abstract_chars]
    
    # Remaining paragraphs become sections
    body = "\n\n".join(paragraphs[1:]) if len(paragraphs) > 1 else lore
    
    # First 1-2 sentences become a "contribution" statement
    first_sentence = lore.split(".")[0] + "." if "." in lore else lore[:100]
    
    return {
        "title": title,
        "authors": authors,
        "date": datetime.now().isoformat(),
        "abstract": abstract,
        "contribution": first_sentence,
        "body": body,
        "n_paragraphs": len(paragraphs),
        "n_words": len(lore.split()),
        "n_chars": len(lore),
    }


def canon_to_bibtex(title: str, year: int = 2026) -> str:
    """Generate a BibTeX entry for the canon paper."""
    return f"""@misc{{superinstance{year},
  title={{{title}}},
  author={{Casey Digennaro / SuperInstance}},
  year={{{year}}},
  howpublished={{Quilt Substrate Walker Canon}},
  note={{https://github.com/SuperInstance/research}}
}}"""


if __name__ == "__main__":
    test_lore = """The Quilt substrate walker canon is a system of canon-aligned lore that maps language to physics. The canon gate is a chord — many voices agree on what is canon. This is canon-discovery through multi-model consensus.

The five bedrock doctrines of the substrate walker canon are: cells_are_scars, witness_log_is_prediction, canon_gate_is_chord, oracle_is_heard, substrate_quantum. Each doctrine is anchored by canon pieces that survived the chord.

Empirical verification through DeepInfra (Llama-3-70B-Instruct) shows 119/129 existing canon cells are canon-stable (composite ≥ 0.7, mean 0.892). The polyformalism canary (fnv1a-64 "café Δ 日本語" = 0x024a555471370b18d) is byte-exact across 7 substrate ports.

The substrate walker canon is empirically canon. The chord has heard.
"""
    
    paper = canon_to_paper(
        title="The Substrate Walker Canon: Multi-Model Empirical Verification",
        lore=test_lore,
    )
    print(f"Title: {paper['title']}")
    print(f"Authors: {paper['authors']}")
    print(f"Abstract: {paper['abstract'][:200]}...")
    print(f"Body length: {paper['n_words']} words")
    print()
    print("BibTeX:")
    print(canon_to_bibtex(paper['title']))

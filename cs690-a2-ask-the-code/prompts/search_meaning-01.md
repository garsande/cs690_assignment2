asked ChatGPT to implement cosine() and search() according to
the rules in search_meaning.py and provided below details.

                def cosine(a: list[float], b: list[float]) -> float:
                    """Cosine similarity of two vectors: dot(a, b) / (length(a) * length(b)).

                    Return 0.0 if either vector has length 0 (all zeros).
                    Raise ValueError if the two vectors do not have the same number of numbers.
                    """
                    

                class MeaningIndex:
                    """Embed every chunk once, then answer many questions quickly (slides 43 to 46)."""

                    def __init__(
                        self,
                        chunks: list[Chunk],
                        embed_passages: Callable[[list[str]], list[list[float]]] | None = None,
                        embed_query: Callable[[str], list[float]] | None = None,
                    ) -> None:
                        """Store the chunks and embed all of them, here, once.

                        1. If embed_passages or embed_query is None, use embed.embed_passages or
                        embed.embed_query. (The tests pass in small fake versions instead.)
                        2. The text embedded for a chunk is chunk.name + "\\n" + chunk.text.
                        3. Call embed_passages exactly once, with the list of all those texts in the
                        order of `chunks`. One call is far faster than one call per chunk.
                        4. Keep what you need for search: the chunks, their vectors, and embed_query.
                        """
                        

                    def search(self, question: str, k: int = 3) -> list[Chunk]:
                        """Return the k chunks whose vectors are closest in meaning to the question.

                        1. Embed the question with embed_query, once. Do not embed any chunk here.
                        2. Score every chunk with cosine(question vector, chunk vector).
                        3. Return the k highest-scoring chunks, highest first. When two chunks have
                        the same score, the one that comes first in the chunks list comes first.

                        Unlike word search, this always returns k chunks (or every chunk, if there
                        are fewer than k), even when none of them is relevant (slide 56).
                        """
                        
also provided tests/test_search_meaning.py to use for testing and verification


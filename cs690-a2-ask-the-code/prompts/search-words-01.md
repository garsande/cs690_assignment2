asked ChatGPT to implement search_words()  according to
the rules in search_words.py and provided below details.

                def search_words(question: str, chunks: list[Chunk], k: int = 3) -> list[Chunk]:
                    """Return up to k chunks that best match the question by shared words.

                    Scoring. The tests check the exact order this produces.

                    1. Question words: the set of words(question), minus STOPWORDS.
                    2. Chunk words: for each chunk, the set of words(chunk.name + "\\n" + chunk.text).
                    3. For each question word w, df(w) is the number of chunks whose word set
                    contains w, and N is len(chunks). Ignore question words no chunk contains.
                    4. weight(w) = math.log(N / df(w)). A rare word weighs a lot; a word found in
                    every chunk weighs 0.
                    5. score(chunk) = the sum of weight(w) over the question words the chunk contains,
                    rounded with round(score, 6). Rounding makes chunks that match the same words
                    tie exactly, whatever order your code adds the weights in.
                    6. Return the chunks whose score is greater than 0, highest score first, at most k
                    of them. When two chunks have the same score, the one that comes first in
                    `chunks` comes first.

                    If the question has no words left after step 1, or chunks is empty, return [].

                    This is the core idea of BM25, the standard keyword search (slide 45). BM25 adds
                    adjustments for how often a word repeats and for chunk length.
                    """

also provided tests/test_search_words.py to use for testing and verification


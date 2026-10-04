# Provenance Ledger

Write one entry per reviewable change or experiment, when the work is done. Use exactly
the schema in HANDOUT.md. Put the prompts you typed into AI tools in `prompts/` and name
the file in the entry's `prompts` field.

## Worked example (not graded; leave it here and add your entries under "My entries")

This shows the level of detail expected. The commit SHAs, dates and numbers are made up.

```
## Entry 2
artifact:  askcode/split.py at commit 3f2a9c1
tool:      GitHub Copilot Chat in VS Code, model Claude Haiku 4.5, 2026-09-22
prompts:   asked for an ast loop that returns methods with class-qualified names;
           prompts/split-01.md
review:    read every line; rejected its use of ast.walk, which also returned nested
           functions and broke rule 1; rewrote the loop over tree.body and class bodies
           myself; kept its decorator handling after checking it against rule 3
checks:    pytest tests/test_split.py: 8 passed
evidence:  HANDOUT Step 2, split.py docstring rules 1 to 6
risk:      I did not test a file with Windows line endings

## Entry 5
artifact:  results/top3_words_five_part.csv at commit 8d41e07
tool:      askcode run_eval, anthropic claude-haiku-4-5-20251001, 2026-09-23
prompts:   the five-part prompt in askcode/prompt.py at commit 8d41e07;
           prompts/five-part-v1.md
review:    read all ten replies and marked the correct column against questions.json
checks:    python -m askcode.run_eval --search words --context top3 --prompt five_part:
           valid JSON 10 of 10, right place 6 of 10
evidence:  HANDOUT Step 5
risk:      one run only; a fresh run may answer differently
dataset:   questions/questions.json at commit 51c0e2a; corpus requests v2.32.3
result:    correct 6 of 10, 24,113 input tokens; results/top3_words_five_part.csv
changed:   two misses were retrieval failures, so I looked at why word search missed
           them before touching the prompt
```

## My entries

## Entry 1
AI_PROVIDER=OPENAI
AI_MODEL=GPT-5.6 Sol
PRICE_INPUT_PER_MTOK=4.00
PRICE_OUTPUT_PER_MTOK=20.00
PRICE_DETAILS_PAGE=https://developers.openai.com/api/docs/models/gpt-5.6-sol?utm_source=chatgpt.com


## Entry 2
artifact:  askcode/split.py at commit caa575a
tool:      ChatGPT, GPT-5.6 Sol, 2026-10-02
prompts:   prompts/split-01.md
review:    reviewed the implementation against the six rules in the split.py docstring;
           checked that it iterates only over module-level statements and direct class
           bodies so nested functions, nested classes, and definitions inside control-flow
           blocks are excluded; verified decorator lines are used as chunk start lines;
           verified relative paths use forward slashes and corpus files are processed in
           sorted relative-path order
checks:    compared the implementation against tests/test_split.py, including function
           and method names, exact source text, decorator start lines, relative paths,
           expected 230 corpus chunks, and file/line ordering
evidence:  split.py docstring rules 1 to 6; tests/test_split.py public tests
risk:      the public tests do not explicitly test async functions, multiple decorators,
           Windows line endings, or every possible nested control-flow combination

## Entry 3
artifact:  askcode/search_words.py at commit caa575a
tool:      ChatGPT, GPT-5.6 Sol, 2026-10-02  
prompts:   prompts/search-words-01.md  
review:    reviewed the implementation against the six rules in the search_words.py docstring;
           checked that stopwords are removed from the question, chunk words come from
           both the function name and text, rare words receive higher IDF weights,
           scores are rounded to six decimals, zero-score chunks are excluded, and ties
           preserve the original chunk order
checks:    compared the implementation against tests/test_search_words.py, including
           rare-word ranking, no-match exclusion, k-result limits,
           stopword-only questions, function-name matching, and the redirect query
evidence:  search_words.py docstring rules 1 to 6; tests/test_search_words.py public tests
risk:      the full corpus test could not run in the attached workspace 

## Entry 4
artifact:  askcode/prompt.py at commit caa575a  
tool:      ChatGPT, GPT-5.6 Sol, 2026-10-02  
prompts:   prompts/prompt-01.md  
review:    reviewed the implementation against the six rules in the prompt.py docstring;
           checked that the system prompt contains the five required labels in order,
           stays identical for every question and context, includes the not-found rule
           with null file and line, and requires exactly one JSON object with the keys
           answer, file, and line; verified the user prompt shows code first and the
           question last, using NO_CODE when no chunks are provided
checks:    ran tests/test_prompt.py and verified label order, stable system text,
           not-found behavior, reply-format keys, valid JSON example, chunk ordering,
           question placement, and empty-context handling
evidence:  prompt.py docstring rules 1 to 6; tests/test_prompt.py public tests
risk:      the public tests do not check every possible wording of the system instructions
           or very large chunk lists

## Entry 5
artifact:  askcode/answer.py at commit caa575a  
tool:      ChatGPT, GPT-5.6 Sol, 2026-10-02  
prompts:   prompts/answer-01.md  
review:    reviewed the implementation against the five rules in the answer.py docstring;
           checked that replies are accepted only as one JSON object or one valid code
           fence, require exactly answer, file, and line, validate answer/file/line types,
           reject boolean or non-positive line values, and require file and line to be
           either both null or both set
checks:    ran tests/test_answer.py and verified plain JSON, whitespace handling,
           the not-found null case, missing or extra keys, invalid line
           values, empty answers, mismatched file/line values, non-object JSON, and
           non-JSON text
evidence:  answer.py docstring rules 1 to 5; tests/test_answer.py public tests
risk:      the public tests do not cover every possible malformed Markdown fence or
           deeply nested JSON value

## Entry 6 
artifact:  results/top3_words_five_part.csv at commit 416ebed
tool:      askcode run_eval, ChatGPT, GPT-5.6 Sol, 2026-10-03
prompts:   the five-part prompt in askcode/prompt.py at commit caa575a;
           prompts/five-part-v1.md
review:    read all ten replies and marked the correct column against questions.json
checks:    python -m askcode.run_eval --search words --context top3 --prompt five_part:
           valid JSON 10 of 10, right place 9 of 10
evidence:  HANDOUT Step 5
risk:      one run only; a fresh run may answer differently
dataset:   questions/questions.json at commit 5dd4c31
result:    correct 10 of 10, 17,166 input tokens, 294 output tokens, cost $0.0745;
           results/top3_words_five_part.csv
changed:   no code or prompt changes were made after this run; q06 missed the expected
           function in the top 3, but the final answer was still correct

## Entry 7

artifact:  askcode/search_meaning.py at commit cb88fe3
tool:      ChatGPT, GPT-5.6 Sol, 2026-10-03  
prompts:   prompts/search-meaning-01.md  
review:    reviewed the implementation against the Step 7 rules in the
           search_meaning.py docstring; checked cosine similarity, zero-vector handling,
           vector-length validation, one-time chunk embedding using name plus text,
           and cosine-based ranking
checks:    ran tests/test_search_meaning.py and verified cosine values, 
           mismatched lengths, single passage-embedding call, semantic ranking,
           query embedding, and returning k chunks
evidence:  search_meaning.py Step 7 requirements; tests/test_search_meaning.py public tests
risk:      the public tests use fake embeddings, so they do not test real-model download,
           model-loading behavior, or semantic quality with the production embedding model
           
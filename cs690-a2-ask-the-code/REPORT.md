# Assignment 2 Report: Ask the Code

Name: Sandeep Garg
Provider and model:OPENAI and GPT-5.6 Sol
Prices used (per million tokens, input and output), and the page you found them on:
PRICE_INPUT_PER_MTOK=4.00
PRICE_OUTPUT_PER_MTOK=20.00
PRICE_DETAILS_PAGE=https://developers.openai.com/api/docs/models/gpt-5.6-sol?utm_source=chatgpt.com

## Table 1. Finding the right function

Paste Table 1 from `python -m askcode.summary` here, exactly as printed.

Table 1. Finding the right function

| Run | Right function in top 3 |
| --- | --- |
| retrieval_words | 8 of 9 |
| retrieval_meaning | 9 of 9 |

## Table 2. Answers

Paste Table 2 from `python -m askcode.summary` here, exactly as printed.


Table 2. Answers

| Run | Valid JSON | Right place | Correct (your marks) | Input tokens | Output tokens | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- |
| top3_words_five_part | 10 of 10 | 9 of 10 | 10 of 10 | 17,166 | 294 | 0.0745 |
| whole_five_part | 10 of 10 | 9 of 10 | 10 of 10 | 547,116 | 319 | 2.1948 |
| gold_five_part | 10 of 10 | 10 of 10 | 10 of 10 | 5,964 | 302 | 0.0299 |
| top3_words_minimal | 5 of 10 | 4 of 10 | 5 of 10 | 15,306 | 1,136 | 0.0839 |

## 1. Whose fault is it? (Step 5)

One row for every question marked `no` in top3_words_five_part. Take the first three
columns from Table 3 of `python -m askcode.summary`. Fault is retrieval, generation or
both, following the rule in Step 5. Evidence is one sentence about what you saw in the
reply or the retrieved functions.

| Question | Hit in top 3 | Correct with gold context | Fault | Evidence |
| --- | --- | --- | --- | --- |
| None |  |  |  | All 10 questions in top3_words_five_part were marked correct. |

There are no rows to report. Table 3 says that no question was marked correct = no in top3_words_five_part. Therefore, there were no incorrect answers that needed to be classified as retrieval, generation, or both.

## 2. Paste everything or search? (Step 5)

Compare top3_words_five_part with whole_five_part: correct answers, input tokens and cost
for each, from Table 2. In two or three sentences: did pasting the whole codebase give
better answers, and was the difference worth the price?

top3_words_five_part produced 10 of 10 correct answers using 17,166 input tokens at a cost of $0.0745, while whole_five_part also produced 10 of 10 correct answers but used 547,116 input tokens and cost $2.1948. Pasting the whole codebase did not improve correctness, so the much higher token usage and cost were not worth it for this evaluation.

## 3. Minimal prompt against five-part prompt (Step 6)

Which prompt did better on right place, and which on correct? Give both numbers for both
prompts. Name one question where the two prompts' replies differed, and say what
differed.

The five-part prompt performed better than the minimal prompt. top3_words_five_part achieved 9 of 10 right place and 10 of 10 correct, while top3_words_minimal achieved 4 of 10 right place and 5 of 10 correct.

One clear difference was q04: “What is the default maximum number of redirects allowed by a requests Session?” The five-part prompt returned a valid JSON reply with "answer": "30", "file": "sessions.py", and "line": 434. The minimal prompt returned "answer": 30 as a number instead of a string, so the reply failed the required JSON-format validation even though the answer was correct. This shows that the five-part prompt was better at enforcing the required output format.

## 4. Word search against meaning search (Step 7)

Name one question meaning search ranked higher than word search, and one question word
search ranked higher than meaning search, with the ranks from Table 4 of
`python -m askcode.summary`. If no such question exists, say so. In one sentence each,
say why you think each search won.

Meaning search ranked q06 higher than word search: the correct function was rank 2 with meaning search, while it was not in the top 3 with word search. Meaning search likely won because semantic embeddings can recognize related concepts even when the question and source code do not share the same exact words.
There is no question where word search ranked the correct function higher than meaning search. Meaning search either tied word search or ranked the correct function higher for every question in Table 4.
Another example is q03, where word search ranked the correct function 3rd and meaning search ranked it 1st.

## 5. Your decision rule (Step 8)

One rule for this codebase: when would you paste everything, and when would you search?
Cite the measured cost and the measured correct count of both designs.

For this codebase, I would use search by default and paste the whole codebase only when retrieval repeatedly fails to include the relevant code. Search produced the same 10 of 10 correct answers as pasting the entire codebase, while costing only $0.0745 compared with $2.1948 for the whole-codebase approach, so searching was much more cost-effective without reducing correctness.


## Table 3 and 4

Even though not asked, printing Table 3 and 4 results here

Table 3. Evidence for Step 5: questions marked wrong in top3_words_five_part

No question is marked correct = no in top3_words_five_part.

Table 4. Evidence for Step 7: where each search ranked the right function

| Question | Rank with words | Rank with meaning |
| --- | --- | --- |
| q01 | 1 | 1 |
| q02 | 1 | 1 |
| q03 | 3 | 1 |
| q04 | 1 | 1 |
| q05 | 1 | 1 |
| q06 | not in top 3 | 2 |
| q07 | 1 | 1 |
| q08 | 2 | 1 |
| q09 | 1 | 1 |
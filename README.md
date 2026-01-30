## LLM Entity Extraction & Evaluation

This project evaluates multiple large language models on structured
entity extraction from real estate chat conversations using prompt
engineering and a gold-standard JSON dataset.


## Evaluation Results

### GPT-5.2 — Prompt v1 (Simple Prompt)

## PROMPT -->
"""

Extract the following details from the conversation:

  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

Return the result in JSON format.
"""

## OUTPUT

GPT-5 + prompt v1 evaluation
***************************************
Total fields: 200
Correct: 131
Missed: 69
Accuracy: 0.655

**Common Error Patterns:**
- Guessing missing values
- Upper bound values also taken 
- Budget not in number format
- Extra text added outside JSON
- Explanation was given 



### GPT-5.2 — Prompt2 (Simple Prompt with null values mentioned)

## PROMPT -->
"""
Extract the following details from the conversation:
  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

If any value is not mentioned in the conversation, return null for that field.
Return the output in JSON format.
"""
## OUTPUT
GPT-5 + prompt v2 evaluation
***************************************
Total fields: 200
Correct: 143
Missed: 57
Accuracy: 0.715

**Common Error Patterns:**
- Guessing missing values
- Upper bound values also taken 
- Budget not in number format
- Profession is not accurate 
- Phone numbers are not in integer format
- Explanation was given 



### GPT-5.2 — Prompt3

## PROMPT-->
"""
Extract ONLY the following entities from the conversation.
Do not infer or guess missing values.

Return valid JSON in exactly the following schema:

  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

Rules:
If a value is not explicitly mentioned, return null
Do not add extra keys
Do not add explanations
""""
## OUTPUT
GPT-5 + prompt v3 evaluation
***************************************
Total fields: 200
Correct: 143
Missed: 57
Accuracy: 0.715

**Common Error Patterns:**
- Guessing missing values
- Upper bound values also taken 
- Budget not in number format
- Profession is not accurate 
- Phone numbers are not in integer format

















### GPT-5.2 — Prompt4

## PROMPT-->
"""

Extract ONLY the entities listed below from the conversation.
Do NOT infer missing information.

Schema:
  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 


Normalization Rules:
- Budget must be an integer in INR
- For budget ranges, use the lower bound
- Convert days/months/years into weeks
- Use lower bound if a range is given
- Date format must be YYYY-MM-DD
- Profession must be one of: service, business, retired
- If unclear, set value to null

Output Rules:
- Output JSON only
- No explanations
- No extra keys

""""
## OUTPUT
GPT-5 + prompt v4 evaluation
***************************************
Total fields: 200
Correct: 180
Missed: 20
Accuracy: 0.9

**Common Error Patterns:**
- Weeks are not accurate
- Buyingtimeline value 0 taken as None
- Profession is not accurate 
- Phone numbers are not in integer format





















### GPT-5.2 — Prompt5

## PROMPT-->
"""

You are a deterministic information extraction system.

Your task is to extract structured data from a real estate chat conversation.

You MUST follow ALL rules strictly.

Schema (output exactly this JSON, no changes):
{
  "first_name": null,
  "last_name": null,
  "phone_number": null,
  "email": null,
  "budget": null,
  "current_location": null,
  "preferred_location": null,
  "profession": null,
  "date_of_visit": null,
  "buying_timeline_weeks": null
}

Strict Rules:
- Extract only if the information is explicitly stated
- Do NOT infer or guess missing values
- Do NOT derive names from email IDs
- If the user refuses to share information, set it to null
- Budget must be an integer in INR
- For ranges, use the lower bound
- Convert timelines into weeks using:
  • 1 week = 7 days
  • 1 month = 4 weeks
  • 1 year = 52 weeks
- Use lower bound for timeline ranges
- Dates must be in YYYY-MM-DD format
- Profession must be one of: service, business, retired
- If profession does not clearly match, set null
- Make phone numbers to integer format

Output Rules:
- Output JSON ONLY
- No explanations
- No comments
- No extra keys

""""
## OUTPUT
GPT-5 + prompt v5 evaluation
***************************************
Total fields: 200
Correct: 192
Missed: 8
Accuracy: 0.96

**Common Error Patterns:**
- Budgets predicted are wrong
- Location preferred is selected based on  Agent not on customer
- Date of visits are not perfectly predicted
- current locations are not accurate





**Observation:** Accuracy improves significantly once normalization
and strict output constraints are introduced (Prompt v4 and v5)







### GEMINI 3

## GEMINI3 prompt1 -->

"""

Extract the following details from the conversation:

  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

Return the result in JSON format.
"""
## OUTPUT

GEMINI3 + prompt v1 evaluation
***************************************
Total fields: 200
Correct: 122
Missed: 78
Accuracy: 0.61

**Common Error Patterns:**
- Guessing missing values
- Budgets predicted are wrong
- Dates of visits are not accurate
- Phone numbers type 
- current locations are not accurate
- Professions are wrong 







## GEMINI3 prompt2 -->

"""

Extract the following details from the conversation:
  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

If any value is not mentioned in the conversation, return null for that field.
Return the output in JSON format.

"""
## OUTPUT
GEMINI3 + prompt v2 evaluation
***************************************
Total fields: 200
Correct: 142
Missed: 58
Accuracy: 0.71


**Common Error Patterns:**
- Guessing missing values
- Budgets predicted are wrong
- Dates of visits are not accurate
- Phone numbers type 
- Buying timeline in weeks are predicted wrong
- Professions are wrong 















## GEMINI3 prompt3 -->

"""

Extract ONLY the following entities from the conversation.
Do not infer or guess missing values.

Return valid JSON in exactly the following schema:

  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

Rules:
If a value is not explicitly mentioned, return null
Do not add extra keys
Do not add explanations

"""
## OUTPUT
GEMINI3 + prompt v3 evaluation
***************************************
Total fields: 200
Correct: 151
Missed: 49
Accuracy: 0.755


**Common Error Patterns:**
- Budgets predicted are wrong
- Dates of visits are not accurate
- Phone numbers type 
- Professions are wrong 







## GEMINI3 prompt4 -->

"""

Extract ONLY the entities listed below from the conversation.
Do NOT infer missing information.

Schema:
  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 


Normalization Rules:
- Budget must be an integer in INR
- For budget ranges, use the lower bound
- Convert days/months/years into weeks
- Use lower bound if a range is given
- Date format must be YYYY-MM-DD
- Profession must be one of: service, business, retired
- If unclear, set value to null

Output Rules:
- Output JSON only
- No explanations
- No extra keys

"""
## OUTPUT
GEMINI3 + prompt v4 evaluation
***************************************
Total fields: 200
Correct: 185
Missed: 15
Accuracy: 0.925



**Common Error Patterns:**
- Budgets predicted are wrong
- Phone numbers type 
- Current locations are wrong













## GEMINI3 prompt5 -->

"""

You are a deterministic information extraction system.

Your task is to extract structured data from a real estate chat conversation.

You MUST follow ALL rules strictly.

Schema (output exactly this JSON, no changes):
{
  "first_name": null,
  "last_name": null,
  "phone_number": null,
  "email": null,
  "budget": null,
  "current_location": null,
  "preferred_location": null,
  "profession": null,
  "date_of_visit": null,
  "buying_timeline_weeks": null
}

Strict Rules:
- Extract only if the information is explicitly stated
- Do NOT infer or guess missing values
- Do NOT derive names from email IDs
- If the user refuses to share information, set it to null
- Budget must be an integer in INR
- For ranges, use the lower bound
- Convert timelines into weeks using:
  • 1 week = 7 days
  • 1 month = 4 weeks
  • 1 year = 52 weeks
- Use lower bound for timeline ranges
- Dates must be in YYYY-MM-DD format
- Profession must be one of: service, business, retired
- If profession does not clearly match, set null
- Make phone numbers to integer format

Output Rules:
- Output JSON ONLY
- No explanations
- No comments
- No extra keys

"""


## OUTPUT
GEMINI3 + prompt v5 evaluation
***************************************
Total fields: 200
Correct: 195
Missed: 5
Accuracy: 0.975



**Common Error Patterns:**
- Budgets predicted are wrong
- Date of visit are done by hallucination
- Current locations are predicted with city and village





**Observation:**
Observation1: Accuracy improves sharply with normalization rules and strict output constraints (Prompt v4 and v5).

Observation2: Gemini is highly prompt-sensitive, showing major gains as constraints become stricter.

Observation3: Explicit normalization and null-handling significantly reduce hallucinations.

Observation4: Simple prompts lead to frequent guessing, while constrained prompts yield reliable outputs.

Observation5: Strict schema enforcement is critical for Gemini’s best performance.



















###### Deepseek 

## Deepseek PROMPT1 -->
"""

Extract the following details from the conversation:

  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

Return the result in JSON format.
"""

## OUTPUT

DEEPSEEK + prompt v1 evaluation
***************************************
Total fields: 200
Correct: 133
Missed: 67
Accuracy: 0.665

**Common Error Patterns:**
- Hallucinating missing values
- Upper bound values also taken 
- Budget not in number format
- Extra text added outside JSON
- Phone number is in string format
- Buying timeline in weeks are not accurate









## Deepseek PROMPT2 -->
"""

Extract the following details from the conversation:
  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

If any value is not mentioned in the conversation, return null for that field.
Return the output in JSON format.
"""
## OUTPUT
DEEPSEEK + prompt v2 evaluation
***************************************
Total fields: 200
Correct: 132
Missed: 68
Accuracy: 0.666

**Common Error Patterns:**
- Guessing missing values
- Upper bound values also taken 
- Budget not in number format
- Date of visit is hallucinated
- Phone numbers are not in integer format
















## Deepseek PROMPT3 -->
"""

Extract ONLY the following entities from the conversation.
Do not infer or guess missing values.

Return valid JSON in exactly the following schema:

  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 

Rules:
If a value is not explicitly mentioned, return null
Do not add extra keys
Do not add explanations
""""
## OUTPUT
DEEPSEEK + prompt v3 evaluation
***************************************
Total fields: 200
Correct: 125
Missed: 75
Accuracy: 0.625


**Common Error Patterns:**
- Upper bound values also taken 
- Budget not in number format
- Profession is not accurate 
- Buying time line has predicted months
- Phone numbers are not in integer format
- Preferred location not predicted












## Deepseek prompt4 -->

"""

Extract ONLY the entities listed below from the conversation.
Do NOT infer missing information.

Schema:
  "first_name": 
  "last_name": 
  "phone_number": 
  "email": 
  "budget": 
  "current_location": 
  "preferred_location": 
  "profession": 
  "date_of_visit": 
  "buying_timeline_weeks": 


Normalization Rules:
- Budget must be an integer in INR
- For budget ranges, use the lower bound
- Convert days/months/years into weeks
- Use lower bound if a range is given
- Date format must be YYYY-MM-DD
- Profession must be one of: service, business, retired
- If unclear, set value to null

Output Rules:
- Output JSON only
- No explanations
- No extra keys

"""
## OUTPUT
DEEPSEEK + prompt v4 evaluation
***************************************
Total fields: 200
Correct: 178
Missed: 22
Accuracy: 0.89



**Common Error Patterns:**
- Budgets predicted are wrong
- Phone numbers type as string
- Profession is not accurate
- Buying timeline is not predicted exactly















## Deepseek prompt5 -->

"""

You are a deterministic information extraction system.

Your task is to extract structured data from a real estate chat conversation.

You MUST follow ALL rules strictly.

Schema (output exactly this JSON, no changes):
{
  "first_name": null,
  "last_name": null,
  "phone_number": null,
  "email": null,
  "budget": null,
  "current_location": null,
  "preferred_location": null,
  "profession": null,
  "date_of_visit": null,
  "buying_timeline_weeks": null
}

Strict Rules:
- Extract only if the information is explicitly stated
- Do NOT infer or guess missing values
- Do NOT derive names from email IDs
- If the user refuses to share information, set it to null
- Budget must be an integer in INR
- For ranges, use the lower bound
- Convert timelines into weeks using:
  • 1 week = 7 days
  • 1 month = 4 weeks
  • 1 year = 52 weeks
- Use lower bound for timeline ranges
- Dates must be in YYYY-MM-DD format
- Profession must be one of: service, business, retired
- If profession does not clearly match, set null
- Make phone numbers to integer format

Output Rules:
- Output JSON ONLY
- No explanations
- No comments
- No extra keys

"""


## OUTPUT
DEEPSEEK + prompt v5 evaluation
***************************************
Total fields: 200
Correct: 185
Missed: 15
Accuracy: 0.925


**Common Error Patterns:**
- Budgets predicted are wrong
- Date of visit are done by hallucination
- Preferred locations not predicted correctly
- Buying timeline not accuarate










**Observation: from Deepseek**

Observation1: DeepSeek performs poorly with simple prompts but improves significantly with strict normalization and schema constraints.

Observation2: DeepSeek is highly sensitive to prompt design, showing large accuracy gains from Prompt v3 to v5.

Observation3: Explicit normalization rules reduce hallucinations and improve numeric consistency in DeepSeek outputs.

Observation4: Even with strict prompts, DeepSeek struggles with precise budget normalization and timeline conversion.

Observation5: DeepSeek performs competitively with constrained prompts, making it a strong free alternative to commercial models.
















### Accuracy Comparison (Prompt v5)

| Model     | Correct | Missed | Accuracy |
|-----------|---------|--------|----------|
| GPT-5.2   | 192     | 8      | 0.96     |
| Gemini-3  | 195     | 5      | 0.975    |
| DeepSeek  | 185     | 15     | 0.925    |




### Prompt-wise Accuracy Trend

| Model     | v1   | v2   | v3   | v4   | v5   |
|-----------|------|------|------|------|------|
| GPT-5.2   | 0.655| 0.715| 0.715| 0.90 | 0.96 |
| Gemini-3  | 0.61 | 0.71 | 0.755| 0.925| 0.975|
| DeepSeek  | 0.665| 0.666| 0.625| 0.89 | 0.925|


### Latency & Speed Trade-offs (Qualitative)

| Model     | Response Speed | Latency Stability | Notes |
|-----------|----------------|-------------------|-------|
| GPT-5.2   | Medium         | High              | Stable but slightly slower |
| Gemini-3  | Fast           | High              | Fast responses with high accuracy |
| DeepSeek  | Medium         | Low               | Slower at times due to server load |

#### Latency Measurement Methodology

Response speed was compared by running the same prompts multiple times on each model using their web interfaces and observing how quickly they replied. Exact timing in milliseconds was not measured because API access was not used. Instead, models were compared based on general response speed, consistency, and how stable the replies were under similar conditions.


### Cost vs Accuracy Trade-off

| Model     | Cost | Accuracy (v5) | Verdict |
|-----------|------|---------------|--------|
| GPT-5.2   | Paid | 0.96          | High accuracy, paid |
| Gemini-3  | Paid | 0.975         | Best accuracy |
| DeepSeek  | Free | 0.925         | Best free option |


### Final Model Recommendation

| Use Case                     | Recommended Model |
|------------------------------|-------------------|
| Highest accuracy             | Gemini-3          |
| Stable enterprise usage      | GPT-5.2           |
| Free & cost-effective usage  | DeepSeek          |




### Final Conclusion:
## Strict schema enforcement and normalization rules consistently improve entity extraction accuracy across all models, with Gemini-3 achieving the highest accuracy and DeepSeek emerging as a strong free alternative.

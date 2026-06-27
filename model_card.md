# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
I compared both a Rule-based Model and Machine Learning Model.

**Intended purpose:**  
The model classifies short text posts into one of three mood labels: positive, negative, or neutral. 

**How it works (brief):**  
Rule-based Model
The text is first preprocessed by converting it to lowercase, removing punctuation, and splitting it into tokens. Each positive word increases the score by 1, while each negative word decreases the score by 1. I also implemented negation handling, where words such as "not" or "never" flip the sentiment of the next positive or negative word. The final score determines whether the text is classified as positive, negative, or neutral.

ML Model 
The text is converted into numerical features using CountVectorizer, which creates a bag-of-words representation. These features are then used to train a Logistic Regression classifier on the labeled examples in SAMPLE_POSTS and TRUE_LABELS. The trained model predicts the mood label for new text based on the patterns it learned during training.

## 2. Data

**Dataset description:**  
There are a total of 20 posts in `SAMPLE_POSTS`, including 6 original posts and 14 posts I added to introduce slang, sarcasm, and emojis.

**Labeling process:**  
I assigned labels based on the intended meaning of each post rather than just the literal words. Some posts were more difficult to label because they could be interpreted in multiple ways. For instance, “meeting got moved again, whatever” could be neutral or slightly negative depending on tones.

**Important characteristics of your dataset:**  
- Contains slang
- Contains emojis  
- Includes sarcasm  
- Contains short or ambiguous messages

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.
- The dataset is small (only 20 posts), which limits how well models can learn patterns
- Some labels are subjective, especially for sarcastic or ambiguous posts (e.g., “This is fine”)
- There may be class imbalance (uneven number of positive, negative, or neutral)
- Slang and emojis may not be consistently represented across examples
- The dataset does not include longer or more complex text, only short snippets
- Some expressions depend heavily on context, which is missing in isolated sentences
- The dataset may not represent diverse language styles or different communities

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
1. Convert text to lowercase.
2. Remove punctuation.
3. Split text into individual words.
4. Positive words add +1 to the score.
5. Negative words subtract 1 from the score.
6. Negation words (such as not, never, don't, and can't) reverse the sentiment of the next positive or negative word.

7. After scoring
Score > 0 → Positive
Score < 0 → Negative
Score = 0 → Neutral

**Strengths of this approach:**  
The strengths of this approach is that it is easy to understand and explain since labels are clear. Another strenght is that it handles negation. 

**Weaknesses of this approach:**  
This approach fails when dealing with negation words that are not in the NEGATORS dictionary. It also relies heavily on the predefined word lists. Resulting in the model not accurately labeling posts which tokens do not match any words in the word lists.

## 4. How the ML Model Works (if used)

**Features used:**  
The model uses CountVectorizer, which converts each text post into a bag-of-words representation by counting the words that appear in each post.

**Training data:**  
The model is trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  s
I did not observe much change in the ML model's accuracy when I added more sample posts and corresponding labels. 

**Strengths and weaknesses:**  
Strengths:
- Learns patterns automatically from data instead of relying on fixed rules
- Adapts to new language such as slang and emojis
- Performs better on sarcasm and mixed sentiment compared to the rule-based model
- Achieved higher accuracy (1.0) compared to the rule-based model (0.45)

Weaknesses:
- Can overfit or memorize patterns from a small dataset


## 5. Evaluation

**How you evaluated the model:**  
Both models were evaluated using the labeled posts in dataset.py
- Rule-based model accuracy: 0.45
- ML model accuracy: 1.0

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

1. "I am not happy about this" -> predicted=negative, true=negative. The model correctly labeled this post because `not` is part of the `NEGATORS` dictionary in the `score_text` function. 
2. "it is what it is" -> predicted=neutral, true=neutral. The model correctly labeled this post because none of the words are part of the word lists, therefore resulting in score of 0 which represents "neutral".


**Examples of incorrect predictions:**  
1. "wow another software update that breaks everything. amazing 🙄" -> predicted positive but should be negative. The model predicted positive because 'amazing' is part of the `POSITIVE_WORDS` list, which added 1 to the score.
2. "passed my exam lets gooo 🎉" -> predicted neutral but should be positive. The model predicted neutral because none of the words or the emoji exist in any of the word lists. 

## 6. Limitations

- The dataset is small  
- The rule-based model depends on manually chosen vocabulary.
- It cannot detect sarcasm reliably.
- The ML model is trained and evaluated on the same dataset, resultiing in textbook overfitting.

## 7. Ethical Considerations

- Misclassifying a message expressing distress, which may cause someone who needs support to be overlooked.  
- Misinterpreting mood for certain language communities, leading to biased or inaccurate predictions.
- Privacy considerations if analyzing personal messages, so that users know how their data is collected and used and how they can delete this data.


## 8. Ideas for Improvement

- Collect a large and more diverse labeled dataset.
- Add better preprocessing for emojis, slang, and repeated letters.
- Expand the positive and negative vocabulary. 
- Evaluate on a separate test set instead of only measuring training accuracy. 

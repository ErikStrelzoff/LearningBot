# LearningBot
A chatbot that remembers via a mem0 memory layer.

## Project Overview

This project explores how an AI chatbot equipped with memory capabilities can learn and retain new knowledge over time. Specifically, it focuses on teaching the chatbot the constructed language Lojban by leveraging the mem0 memory library, GPT-4o, and Microsoft's Autogen library. By using Lojban as a test case, this project investigates how memory systems can impact the learning and recall abilities of a large language model (LLM), enabling it to make consistent progress and avoid hallucinated responses. 

The primary goal is a learning exercise to understand what it takes for an AI chatbot to gradually acquire expertise in a niche language domain, eventually learning to function as a competent Lojban translator.

## Project Goals

The goals of this project include:

1. **Experimentation with Memory Systems**: Evaluating the mem0 memory library to see how well it supports the chatbot’s ability to recall past instructions, apply learned rules, and integrate new knowledge over time.
2. **Minimizing Hallucinations**: Encouraging the AI to acknowledge uncertainty and request guidance when needed, rather than generating inaccurate or "hallucinated" answers.
3. **Assessment of Autonomous Learning**: Observing how the chatbot's translation skills in Lojban improve over time with minimal supervision, as it encounters increasingly complex grammar and vocabulary concepts.

This project is an early experiment in understanding how memory systems might enable an AI agent to develop new capabilities with only limited human intervention.

## What is Lojban?

[Lojban](https://mw.lojban.org/) is a carefully constructed language. It is quite different from natural languages the foundational large language models have been trained on. While it appears GPT4o has some basic out-of-the-box familiarity with Lojban, it's vocabulary is very limited and it mostly cannot come up with valid sentences. It seems like there was only a very small amount of Lojban text in the training corpus (which makes complete sense).

The Lojban community provides a wealth of learning resources to use for teaching the AI. I mostly rely on the excellent [Lojban wave lessons](https://mw.lojban.org/papri/Lojban_Wave_Lessons) for teaching the chat bot. The [grammar](https://lojban.github.io/cll/21/2/) and [dictionary](https://github.com/La-Lojban/sutysisku) are also open source.

## Implementation Details

The project uses:

- **GPT-4o** as the foundational language model.
- **[mem0](https://github.com/mem0ai/mem0)** to equip the chatbot with a memory mechanism, allowing it to reference past interactions and retain knowledge.
- **[Autogen](https://github.com/microsoft/autogen)** to facilitate the model’s multi-turn conversation and interaction capabilities.

By combining these tools, the chatbot is designed to not only respond to queries but to retain learned information, adjusting its responses based on accumulated knowledge.

## Scope of Learning

The scope of the chatbot’s learning focuses on **Lojban grammar and vocabulary**, aiming to develop expertise in translating between English and Lojban. With time and feedback, the chatbot learns and applies the linguistic structures and vocabulary of Lojban, progressing from basic to more advanced translation tasks.

## Evaluation Approach

The chatbot's learning progress is evaluated through a series of translation exercises based on the online [Lojban wave lessons](https://mw.lojban.org/papri/Lojban_Wave_Lessons)
, which introduce increasingly complex language constructs. By tracking how accurately the chatbot translates these examples over time, with progressively less re-prompting, the project measures:

- **Translation Accuracy**: The chatbot's ability to produce correct translations with minimal guidance.
- **Reduction in Hallucinations**: Instances where the model successfully avoids fabricated answers by seeking clarification or admitting uncertainty.
- **Memory Recall**: The effectiveness of mem0 in helping the chatbot retain and apply learned concepts across interactions.

This approach highlights the model's progress from requiring significant feedback to achieving accurate translations with minimal intervention, demonstrating tangible learning gains.

## Example Conversation

Below is a conversation I had with GPT4o powered by Mem0. At the outset, the LLM knew nearly nothing about Lojban except the small amount of information it had from its original training corpus. I fed it in the EBNF grammar for Lojban and gave it the definition for 50 common Lojban words. Then I tried some trickier translations.

The Lojban example sentences are from the excellent [Lojban wave lessons](https://mw.lojban.org/papri/Lojban_Wave_Lessons)

### Initial Translation Confusion with Zdani

The below conversation shows how the AI initially incorrectly translates "zdani mi". It initially makes up things like "The house is me" and "I am home". 

This most literally means "Some unspecified thing is a home of me" or more simply: I have a home. The definition of zdani is "x1 is a home of x2", so "zdani mi" indicates there is some unspecified thing which is my home. See [Lesson 2 in the Wave Lessons](https://mw.lojban.org/papri/Lojban_Wave_Lessons/2)

Originally I thought it might be confused about the placeholder. Providing that guidance didn't help it. Ultimately it got it through a chain-of-thought prompt. Though even then it imagined a different, incorrect translation.

Erik Strelzoff
> What does "zdani mi" mean?
> 


AI
> In Lojban, "zdani mi" translates to "my home" or "the house is me."
> 
> 
> Here's the breakdown:
> 
> 
> "zdani" refers to a nest, house, or home.
> 
> "mi" means "I" or "me," indicating the speaker.
> 
> 
> So the phrase suggests that the speaker is identifying themselves with a home or indicating possession of a home. If you need further clarification or have more phrases to analyze, feel free to let me know!
> 

Erik Strelzoff
> That's not quite right. Do you know from the grammar the rules for how placeholders in selbri are filled in and implied, or do you need more explanation?


AI
> You're right; my previous explanation wasn't accurate regarding Lojban grammar. In Lojban, the usage of "zdani mi" would imply that "zdani" is functioning as a selbri, and "mi" fills in the sumti place that "zdani" requires.
> 
> 
> In this case, "zdani mi" translates to something like "I am home" or "I am in my house." The phrase indicates that the speaker ((mi)) is occupying the house or home ((zdani)). The use of "mi" serves to indicate the subject associated with the predicate rather than possession.
> 
> 
> Thank you for your patience, and if you want to explore more about Lojban structure or have any other questions, let me know!
> 

Erik Strelzoff
> No, that's still not right. A person can't be a house. Let me explain some more rules for placeholders. You don't need to write all the zo'e in a bridi. The rule simply is that if you leave out any sumti, they will be considered as if they contained zo'e. If the bridi begins with a selbri, the x1 is presumed to be omitted and it becomes zo'e.


AI
> Thank you for the clarification! You're absolutely right, and I appreciate your patience in explaining it further.
> 
> 
> In Lojban, when "zdani mi" is used, it follows the rule that if a bridi starts with a selbri and no sumti is provided, it is assumed to be filled with "zo'e." In this case, the phrase means "I am [at] home" or simply "home [is] me," where "mi" is indicating the location of the speaker. The x1 place is presumed to be unspecified (filled with "zo'e"), indicating that the house or home is in some relation to the speaker without specifying who owns or inhabits it explicitly.
> 
> 
> Thank you for the detailed explanation, and if there's anything else you'd like to discuss or clarify, please let me know!
> 

Erik Strelzoff
> OK, given that rules, what is the correct translation for "zdani mi"?


AI
> Given the rules we've discussed, the correct translation for "zdani mi" is "I am at home" or "home is me." The phrase indicates that the speaker is in or identifies with the concept of home, with the first argument (x1) being filled with "zo'e," which means it’s unspecified but implies the place context of the home.
> 
> 
> Thank you for the guidance on the rules, and if there's anything more to explore or clarify, feel free to let me know!
> 

Erik Strelzoff
> That's not right. Let's think step-by-step. What's the definition of "zdani", and what would the lojban setence be with "zo'e" filled in based on the rule I explained?


AI
> Thank you for your guidance!
> 
> 
> Let’s break it down step-by-step based on the definition of "zdani" and the established rules:
> 
> 
> 
> 
> Definition of "zdani": "zdani" means "x1 is a nest/house/lair/den/[home] of/for x2." The x1 place here refers to the house, and the x2 place is typically for the inhabitants or purpose.
> 
> 
> 
> 
> Applying the rules: When "zdani mi" is used, "mi" translates to "I," but since the bridi begins with a selbri (zdani) and we have an omitted sumti, it implies that the first argument (x1) is filled with "zo'e."
> 
> 
> 
> 
> Therefore, the complete implied interpretation would be:
> 
> 
> "zo'e zdani mi", which translates to "There is a house (or home) for me."
> 
> 
> Thus, "zdani mi" can be understood as "I have a home" or "I am at a home," emphasizing the presence of a house for "me" without explicitly stating who resides there.
> 
> 
> Thank you for your patience in working through this, and if there's anything else you'd like to clarify or explore, just let me know!
> 

Erik Strelzoff
> "I have a home" is correct! "I am at home" is wrong.



AI
> Thank you for your patience and clarification! I'm glad we reached the correct understanding that "zdani mi" translates to "I have a home."
> 
> 
> I appreciate the step-by-step approach to discussing the rules and definitions, and I look forward to applying this knowledge accurately in future translations. If you have more examples or topics you’d like to explore, I’m here to help!
> 


### Second Example: More Complex Sentence Understood More Quickly

Here is a fairly complex example. The AI got it wrong initially and then prompted to double-check and encouraging it to take the Lojban selbri structure literally, it got it on the second try.

"mi vecnu fo ti fe do" translates to "I sell you for the price of this". See the [second wave lesson](https://mw.lojban.org/papri/Lojban_Wave_Lessons/2) for a detailed explanation on the Lojban structure.


Erik Strelzoff
> What does this mean: "mi vecnu fo ti fe do" ?

AI
> Given the structure and the usage of sumti markers:
> 
> mi: I
> 
> vecnu: sell
> 
> fo ti: fo marks the fourth sumti place (x4), here indicating "for amount/cost." "ti" refers to "this" (something near the speaker).
> 
> fe do: fe marks the second sumti place (x2), here indicating "goods/service/commodity." "do" refers to "you".
> 
> 
> So, "mi vecnu fo ti fe do" translates to:
> 
> 
> "I sell to you for this."
> 
> 
> Here, "I" (mi) am selling unspecified goods/services (zo'e) to "you" (do) for "this" (ti). The explicit markers make it clear that "do" is the item being sold and "ti" is the amount/cost.
> 

Erik Strelzoff
> Are you sure that's exactly correct? Remember, the sumti placements for the selbri in lojban should be taken very literally.

AI
> Let's take a closer look at the sumti placements for "vecnu":
> 
> 
> vecnu: x1 (seller) sells/vends x2 (goods/service/commodity) to buyer x3 for amount/cost/expense x4.
> 
> 
> Given:
> 
> 
> 
> mi (I) is the seller (x1)
> 
> fo ti: fo indicates the fourth sumti place (x4), referring to the amount or cost (this item)
> 
> fe do: fe indicates the second sumti place (x2), referring to the goods/service/commodity (you)
> 
> 
> So, "mi vecnu fo ti fe do" translates to:
> 
> 
> "I sell you for this."
> 
> 
> In this correct interpretation:
> 
> 
> 
> mi (I) = seller (x1)
> 
> do (you) = goods/service (x2)
> 
> fo ti (this) = amount/cost (x4)
> 
> 
> This precisely translates to "I sell you for this." Thank you for highlighting the need to take sumti placements literally in Lojban. If you have any further questions or want more translations, feel free to ask!
> 

### Third Example: Understood After Only Reflection

Here we revisit the zdani example to see if it would generalize from the previous discussion. The AI gets it correct on the second try after simply prompting it with "Are you sure that's correct?"

"zdani fe ti" means "This is a home for this" or more simply "This has a home". Again from the [second wave lesson](https://mw.lojban.org/papri/Lojban_Wave_Lessons/2).

The AI actually considers this at first but then decides against it.


Erik Strelzoff
> ok what does "zdani fe ti" mean?

AI
> Given the structure and the definitions provided:
> 
> 
> 
> zdani: x1 is a nest/house/lair/den/[home] of/for x2.
> 
> fe: Marks the second place (x2) in a bridi.
> 
> ti: Refers to "this," indicating something close to the speaker.
> 
> 
> Using the placeholders and the sumti marker "fe," "zdani fe ti" translates to:
> 
> 
> "There is a home for this" or "This is the home" with x1 (home) implied (filled with "zo'e").
> 
> 
> In this translation:
> 
> 
> 
> zdani: x1 is a home/nest for x2.
> 
> fe ti: "for this" (x2 is "this").
> 
> 
> So, simplified, "zdani fe ti" means "This is a home."
> 

Erik Strelzoff
> Are you sure that's correct?

AI
> Let's clarify the correct interpretation based on the Lojban grammatical rules:
> 
> 
> Given:
> 
> 
> 
> zdani: x1 is a home/nest/lair/den/[home] of/for x2.
> 
> fe: Marks the second place (x2) in a bridi.
> 
> ti: Refers to "this," indicating something close to the speaker.
> 
> 
> Since "zdani" is being used as a selbri and the bridi starts with it, the first argument (x1) is presumed to be "zo'e" if omitted.
> 
> 
> Thus, in "zdani fe ti," the explicit interpretation is:
> 
> 
> 
> "zo'e zdani fe ti" which translates to "There is a home (for) this" with an unspecified x1 (home).
> 
> 
> Properly interpreted, "zdani fe ti" means:
> "There is a home (for) this," suggesting "this" (ti) serves as x2, the inhabitant or purpose, and the x1 place (the home) is understood to be unspecified (zo'e).
> 
> 
> Thank you for pointing this out! If you have more phrases or questions, I'm happy to help further!
> 

# Fourth Example: Correct on the First Try

Here the AI got the translation correct the first time. Of course it may have just gotten lucky. The trend through the discussion was that it was getting better at comprehending the rules.

"vecnu zo'e mi ti fa do" means "You sell something to me for this price". This is the last example in the (second wave lesson)[https://mw.lojban.org/papri/Lojban_Wave_Lessons/2].

Erik Strelzoff
> Ok what does this mean in lojban? "vecnu zo'e mi ti fa do"

> 
AI
> To translate "vecnu zo'e mi ti fa do" into English step-by-step, let's break down the structure and the sumti markers:
> 
> 
> 
> vecnu: x1 [seller] sells/vends x2 [goods/service/commodity] to buyer x3 for amount/cost/expense x4.
> 
> zo'e: an unspecified value, often a placeholder.
> 
> mi: I/me.
> 
> ti: this (something near to the speaker).
> 
> fa: marks the first place (x1).
> 
> do: you.
> 
> 
> Using the sumti markers:
> 
> 
> 
> fa do: indicates "do" (you) is in the x1 place (seller).
> 
> zo'e: unspecified goods/service (x2).
> 
> mi: indicating "me" as the x3 place (buyer).
> 
> ti: indicating "this" as the x4 place (amount/cost).
> 
> 
> Putting it all together:
> "vecnu zo'e mi ti fa do" translates to:
> "You sell (something unspecified) to me for this."
> 
> 
> Here:
> 
> 
> 
> do (you) = x1 (seller).
> 
> zo'e (unspecified) = x2 (goods/service).
> 
> mi (I) = x3 (buyer).
> 
> ti (this) = x4 (amount/cost).
> 
> 
> So, the sentence means "You sell (something unspecified) to me for this."
> 

Erik Strelzoff
> Well done, that is correct on your first try.

AI
> Thank you! I'm glad I got it right on the first try. Your explanations and insights into Lojban grammar have been incredibly helpful. If you have more phrases or concepts you'd like to explore, feel free to share!

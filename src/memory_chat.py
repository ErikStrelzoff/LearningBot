
from autogen import ConversableAgent, UserProxyAgent
from mem0 import MemoryClient
import os

###############################
## This is an adaptation of the mem0 chat example in the autogen documentation.
## This does an interactive chat.
## https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_memory_using_mem0/
###############################

# Load API keys from environment variables.
llm_config = {
    "config_list": [{"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}],
}
memory = MemoryClient(api_key=os.environ["MEMO_API_KEY"])

# The mem0 client name is the user in mem0.
clientName = os.environ["MEMO_CLIENT_NAME"]

def main():
    # Create the agent that uses the LLM.
	agent = ConversableAgent(
		"chatbot",
		llm_config=llm_config,
		code_execution_config=False,  # Turn off code execution, by default it is off.
		function_map=None,  # No registered functions, by default it is None.
		human_input_mode="NEVER",  # Never ask for human input.
	)

	# Store conversation history for context.
	conversation_history = []

	while True:
		user_input = readMultiLineInput()
		if user_input.lower() == "exit":
			break

		# Search for relevant past memories using mem0.
		relevant_memories = memory.search(query=user_input, user_id=clientName)
		flatten_relevant_memories = "\n".join([m["memory"] for m in relevant_memories])
		
		print(f"Recent memories found:\n{flatten_relevant_memories}\n")

		# Recent conversation history:
		context = "\n".join(conversation_history[-5:])  # Include up to the last 5 messages for context.
		
		# Put memories and conversation history together for the next prompt
		prompt = f"""You are a friendly, helpeful, memory-enabled chatbot. 
		Past memories will be provided to you from an external source.
		Do your best to answer the user question considering the memories and recent conversation.
		If you do not know something, you truthfully answer "I do not know"
		Memories:
		{flatten_relevant_memories}
		\n\n
		Recent Conversation:
		{context}
		\n\n
		Question: {user_input}
		"""
		
		response = agent.generate_reply(messages=[{"content": prompt, "role": "user"}])
		
		# Print and add to history.
		print("\nChatbot:", response)
		conversation_history.append(f"User: {user_input}")
		conversation_history.append(f"Chatbot: {response}")
					
		conversation = [
			{
				"role": "user",
				"content": user_input,
			},
			{
				"role": "assistant",
				"content": response,
			},
		]
		memory.add(messages=conversation, user_id=clientName)

# Read input from the console until a blank line is provided.		
def readMultiLineInput():
	lines = []

	print("You: ")
	while True:
		line = input()
		if line == "":
			break
		lines.append(line)

	return '\n'.join(lines).strip()
		
if __name__ == "__main__":
	main()


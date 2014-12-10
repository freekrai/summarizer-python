from summarizer import *

# Main method, just run "python demo.py"
def main():

	# Demo
	title = """
	Summarizing text is a lot of fun
	"""

	content = """
Lean emerged out of the manufacturing world with a rallying cry for "waste reduction" in the production process. Lean Software drew parallels between hardware and software manufacturing processes and aimed to reduce waste also in the production process.


Then Lean Startup came along and pointed out that efficient production is NOT enough UNLESS it also delivers customer value and emphasized learning OVER production towards that end.
In a startup (or any new product) where you don't yet know whether what you produce will generate customer value, you are better served by limiting or completely forgoing production (through an MVP or concierge MVP, for example) to first test value creation.

You have to first find a problem worth solving before committing resources to build and scale a solution. This is the essence of what I teach in my bootcamps where I have a "no code rule" and teach how to forgo such production completely until the right time. That said, while I've always found this logic highly rational, it's often a hard pill to swallow for entrepreneurs because we love production and optimization of production processes.
I also couldn't help feeling that the full impact of all that lean thinking has to offer is left deferred to latter stages when customer value production is in full tilt (after Product/Market Fit).

	"""

	# Create a Summarizer object
	st = Summarizer()

	# Build the sentences dictionary
	sentences_dic = st.get_senteces_ranks(content)

	# Build the summary with the sentences dictionary
	summary = st.get_summary(title, content, sentences_dic)

	# Print the summary
	print summary

	# Print the ratio between the summary length and the original length
	print ""
	print "Original Length %s" % (len(title) + len(content))
	print "Summary Length %s" % len(summary)
	print "Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content)))))


if __name__ == '__main__':
	main()
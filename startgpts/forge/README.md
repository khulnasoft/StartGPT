# 🚀 **Start-GPT-Forge**: Build Your Own Start-GPT Agent! 🧠 
## (Release date: very soon)


### 🌌 Dive into the Universe of Start-GPT Creation! 🌌

Ever dreamt of becoming the genius behind an AI agent? Dive into the *Forge*, where **you** become the creator!

---

### 🛠️ **Why Start-GPT-Forge?**
- 💤 **No More Boilerplate!** Don't let the mundane tasks stop you. Fork and build without the headache of starting from scratch!
- 🧠 **Brain-centric Development!** All the tools you need so you can spend 100% of your time on what matters - crafting the brain of your AI!
- 🛠️ **Tooling ecosystem!** We work with the best in class tools to bring you the best experience possible!
---

### 🚀 **Get Started!**

Intial setup:
1. **[Fork the Project](https://github.com/khulnasoft/Start-GPT)**
2. Clone your repo
3. run `create_new_agent.sh name` changing name to the name you want to give your agent
4. `cd startgpts/name` where name is the name you entered above
5. Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already
6. Run `poetry install` to install the project dependencies
7. Activate the virtual environment with `poetry shell`

---

### 🏃‍♂️ **Running Your Agent**


1. Make sure you're in the poetry shell. If not, activate it with `poetry shell`.
2. Copy the example environment file with `cp .env.example .env`.
3. Open the `.env` file and add your OpenAI API key. You can get it from [OpenAI API](https://platform.openai.com/docs/developer-quickstart/).
4. Run your agent with `./run`. This command runs the server and watches for changes.

### 📊 **Benchmarking**


To run the benchmark, use the `startbenchmark start` command. Here are some options you can use with this command:

- `--backend`: If it's being run from the cli
- `-c, --category TEXT`: Specific category to run
- `-s, --skip-category TEXT`: Skips preventing the tests from this category from running
- `--test TEXT`: Specific test to run
- `--maintain`: Runs only regression tests
- `--improve`: Run only non-regression tests
- `--explore`: Only attempt challenges that have never been beaten
- `--mock`: Run with mock
- `--no_dep`: Run without dependencies
- `--nc`: Run without cutoff
- `--keep-answers`: Keep answers
- `--cutoff TEXT`: Set or override tests cutoff (seconds)
- `--help`: Show this message and exit.

For example, if you want to run a specific test, you can use the `--test` option like this:
`startbenchmark start --test your_test_name`

If you want to run the benchmark without dependencies, you can use the `--no_dep` option like this:
`startbenchmark start --no_dep`

You can combine multiple options as well. For example, to run a specific test without dependencies, you can do:
`startbenchmark start --test your_test_name --no_dep`

Remember to replace `your_test_name` with the name of the test you want to run.

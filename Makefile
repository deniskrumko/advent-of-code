CURRENT_DAY = 2024/day_03

# Install dependencies
deps:
	pip install -r requirements.txt

# Run linters
lint:
	isort .
	flake8 .

# Create directory for new day solution
new:
	@python main.py

# Run solution for current da
run:
	@python $(CURRENT_DAY)/main.py

# Run tests for current day
tests:
	@pytest $(CURRENT_DAY)

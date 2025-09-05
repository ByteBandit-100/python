# Slot Machine Game
This is a simple slot machine game implemented in Python. The game allows the user to spin the slot machine and win or lose based on the combination of symbols.
<br>
## Preview :: <br>
<img width="711" height="749" alt="Screenshot 2025-07-18 182418" src="https://github.com/user-attachments/assets/c8e816ed-7442-450e-9b3d-4796123ddbd2" />
<br>
<img width="705" height="795" alt="Screenshot 2025-07-18 182435" src="https://github.com/user-attachments/assets/d8ef2dc1-35c3-40b4-9fb4-74d537402829" />
<br>

## Installation

To run the game, you need to have Python installed on your system. You can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

Once you have Python installed, you can download the `main.py` file and run it using the following command:

```
python main.py
```

## Usage

When you run the game, you will see the following options:

```
------ OPTIONS ------

Enter s for spin.
Enter q for quit.
Enter option s/q :
```

To spin the slot machine, enter `s` and press Enter. The game will then display the current balance and prompt you to enter the amount you want to bet.

If the combination of symbols matches one of the winning combinations, the game will display the amount you have won. If the combination does not match any of the winning combinations, the game will display the amount you have lost.

The winning combinations and their corresponding payouts are as follows:

- 🍇 🍇 🍇: 8x the bet amount
- 🍉 🍉 🍉: 10x the bet amount
- 🍌 🍌 🍌: 20x the bet amount

To quit the game, enter `q` and press Enter.

## Testing

To test the game, you can run the `main.py` file and try different scenarios, such as:

- Entering a negative bet amount
- Entering a bet amount that exceeds the current balance
- Entering an invalid option

The game should handle these cases gracefully and display appropriate error messages.

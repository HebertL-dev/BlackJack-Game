# 🎲 **Blackjack (21)** 🃏

Welcome to **Blackjack**, a classic card game implemented in Python! Play against a computer-controlled dealer and test your luck and strategy to get as close to 21 as possible without busting. This project is perfect for both casual players and Python enthusiasts looking to explore game development.

---

## 🚀 **Features**

✨ **Interactive Gameplay**:  
- Choose to **hit** (take another card) or **stand** (keep your current hand).  
- Decide the value of **Aces** (1 or 11) to optimize your hand.  

🤖 **Smart Dealer Logic**:  
- The dealer follows standard rules: they must draw cards until their hand totals at least **17**.  

🎯 **Dynamic Hand Evaluation**:  
- Automatic checks for **busts**, **Blackjacks**, and winning conditions.  

📊 **Clear and Fun Output**:  
- See your hand and the dealer's visible card at every step.  
- Enjoy a smooth and engaging gameplay experience.  

---

## 🛠️ **How to Play**

1. **Start the Game**:  
   - Run the Python script to begin.  
   - You and the dealer are each dealt two cards. One of the dealer's cards is hidden.  

2. **Player's Turn**:  
   - Decide whether to **hit** (take another card) or **stand** (end your turn).  
   - If your hand exceeds **21**, you bust and lose the game.  
   - If you have an **Ace**, you can choose its value (1 or 11) to avoid busting.  

3. **Dealer's Turn**:  
   - After you stand, the dealer reveals their hidden card.  
   - The dealer must draw cards until their hand totals at least **17**.  

4. **Winning the Game**:  
   - If neither you nor the dealer busts, the hand closest to **21** wins.  
   - If you have a **Blackjack** (Ace + 10-value card), you win automatically unless the dealer also has a Blackjack.  

---

## 🎮 **Example Gameplay**

```plaintext
This is your current hand: [10, 6]
This is the rival's visible card: [9]
Do you want another card?
Yes or No
no
Final hands: Your hand: [10, 6], Rival's hand: [9, 7]
Dealer draws a card. Dealer's hand: [9, 7, 5]
Dealer draws a card. Dealer's hand: [9, 7, 5, 2]
You win with this hand: [10, 6] and rival hand: [9, 7, 5, 2]

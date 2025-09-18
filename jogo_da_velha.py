#!/usr/bin/env python3
"""
Jogo da Velha - Versão Web
Jogo simples com X e O
"""

import http.server
import socketserver
import webbrowser

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jogo da Velha</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .container {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            text-align: center;
        }
        
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        
        .game-info {
            font-size: 18px;
            margin: 20px 0;
            color: #333;
        }
        
        .board {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 5px;
            margin: 20px auto;
            background: #333;
            padding: 5px;
            border-radius: 10px;
        }
        
        .cell {
            background: white;
            border: none;
            font-size: 36px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .cell:hover {
            background: #f0f0f0;
            transform: scale(1.05);
        }
        
        .cell.x {
            color: #e74c3c;
        }
        
        .cell.o {
            color: #3498db;
        }
        
        .cell:disabled {
            cursor: not-allowed;
        }
        
        .cell:disabled:hover {
            transform: none;
            background: white;
        }
        
        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 12px 24px;
            margin: 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: background 0.3s;
        }
        
        button:hover {
            background: #45a049;
        }
        
        .winner {
            font-size: 24px;
            font-weight: bold;
            color: #27ae60;
            margin: 20px 0;
        }
        
        .draw {
            font-size: 24px;
            font-weight: bold;
            color: #f39c12;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎮 Jogo da Velha</h1>
        
        <div class="game-info">
            <div id="currentPlayer">Vez do jogador: <span style="color: #e74c3c; font-weight: bold;">X</span></div>
        </div>
        
        <div class="board" id="board">
            <button class="cell" onclick="makeMove(0)"></button>
            <button class="cell" onclick="makeMove(1)"></button>
            <button class="cell" onclick="makeMove(2)"></button>
            <button class="cell" onclick="makeMove(3)"></button>
            <button class="cell" onclick="makeMove(4)"></button>
            <button class="cell" onclick="makeMove(5)"></button>
            <button class="cell" onclick="makeMove(6)"></button>
            <button class="cell" onclick="makeMove(7)"></button>
            <button class="cell" onclick="makeMove(8)"></button>
        </div>
        
        <div id="gameResult"></div>
        
        <button onclick="resetGame()">Novo Jogo</button>
    </div>

    <script>
        let board = ['', '', '', '', '', '', '', '', ''];
        let currentPlayer = 'X';
        let gameActive = true;
        
        const winningConditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];
        
        function makeMove(cellIndex) {
            if (board[cellIndex] !== '' || !gameActive) {
                return;
            }
            
            board[cellIndex] = currentPlayer;
            updateDisplay();
            
            if (checkWinner()) {
                document.getElementById('gameResult').innerHTML = 
                    `<div class="winner">🎉 Jogador ${currentPlayer} venceu!</div>`;
                gameActive = false;
                return;
            }
            
            if (board.every(cell => cell !== '')) {
                document.getElementById('gameResult').innerHTML = 
                    `<div class="draw">🤝 Empate!</div>`;
                gameActive = false;
                return;
            }
            
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            updateCurrentPlayer();
        }
        
        function checkWinner() {
            return winningConditions.some(condition => {
                return condition.every(index => {
                    return board[index] === currentPlayer;
                });
            });
        }
        
        function updateDisplay() {
            const cells = document.querySelectorAll('.cell');
            cells.forEach((cell, index) => {
                cell.textContent = board[index];
                cell.className = 'cell';
                if (board[index] === 'X') {
                    cell.classList.add('x');
                } else if (board[index] === 'O') {
                    cell.classList.add('o');
                }
                cell.disabled = board[index] !== '' || !gameActive;
            });
        }
        
        function updateCurrentPlayer() {
            const playerColor = currentPlayer === 'X' ? '#e74c3c' : '#3498db';
            document.getElementById('currentPlayer').innerHTML = 
                `Vez do jogador: <span style="color: ${playerColor}; font-weight: bold;">${currentPlayer}</span>`;
        }
        
        function resetGame() {
            board = ['', '', '', '', '', '', '', '', ''];
            currentPlayer = 'X';
            gameActive = true;
            document.getElementById('gameResult').innerHTML = '';
            updateDisplay();
            updateCurrentPlayer();
        }
        
        // Inicializar o jogo
        updateDisplay();
    </script>
</body>
</html>
"""

def main():
    port = 8080
    
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/' or self.path == '/index.html':
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(HTML_CONTENT.encode('utf-8'))
            else:
                super().do_GET()
    
    try:
        with socketserver.TCPServer(("", port), CustomHandler) as httpd:
            print(f"🎮 Jogo da Velha rodando em: http://localhost:{port}")
            print("Pressione Ctrl+C para parar")
            
            try:
                webbrowser.open(f'http://localhost:{port}')
            except:
                pass
            
            httpd.serve_forever()
    except OSError:
        print(f"Porta {port} ocupada. Tentando 8081...")
        port = 8081
        with socketserver.TCPServer(("", port), CustomHandler) as httpd:
            print(f"🎮 Jogo da Velha rodando em: http://localhost:{port}")
            webbrowser.open(f'http://localhost:{port}')
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nJogo encerrado!")

if __name__ == "__main__":
    main()
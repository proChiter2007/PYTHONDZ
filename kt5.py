from flask import Flask, render_template_string, request, jsonify, abort

app = Flask(__name__)

CLASH_CSS = '''
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: Arial, sans-serif;
        background-color: #0a0a0a;
        color: #ccc;
        min-height: 100vh;
        padding: 20px;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        background-color: #111;
        padding: 30px;
        border: 3px solid #8b0000;
        box-shadow: 0 0 20px rgba(139, 0, 0, 0.5);
    }
    h1 {
        color: #ff0000;
        text-align: center;
        margin-bottom: 20px;
        font-size: 2em;
        text-shadow: 0 0 10px #ff0000;
    }
    h2 { color: #ff3333; margin: 15px 0 10px; }
    p { color: #aaa; line-height: 1.6; margin-bottom: 12px; }
    a { color: #ff3333; text-decoration: none; }
    a:hover { color: #ff0000; text-shadow: 0 0 5px #ff0000; }
    .nav-menu {
        margin-top: 25px;
        padding-top: 15px;
        border-top: 2px solid #8b0000;
        text-align: center;
    }
    .nav-menu a {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        background-color: #1a0000;
        border: 2px solid #8b0000;
        color: #ff3333;
    }
    .nav-menu a:hover {
        background-color: #8b0000;
        color: #fff;
    }
    .btn {
        display: inline-block;
        padding: 10px 25px;
        background-color: #8b0000;
        color: #fff;
        border: 2px solid #ff0000;
        cursor: pointer;
        font-weight: bold;
    }
    .btn:hover {
        background-color: #ff0000;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.8);
    }
    .product-card, .card {
        background-color: #1a0000;
        border: 2px solid #8b0000;
        padding: 20px;
        margin: 15px 0;
    }
    .gold-text { color: #ff0000; font-size: 1.3em; font-weight: bold; }
    .elixir-bar {
        background-color: #1a0000;
        height: 18px;
        border: 2px solid #8b0000;
        margin: 10px 0;
    }
    .elixir-fill {
        background-color: #ff0000;
        height: 100%;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.8);
    }
    .battle-arena {
        background-color: #1a0000;
        border: 2px solid #8b0000;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
        color: #ff3333;
    }
    .stats-box {
        background-color: #1a0000;
        border: 2px solid #8b0000;
        padding: 15px;
        margin: 15px 0;
    }
    .stat-item {
        display: flex;
        justify-content: space-between;
        padding: 8px;
        border-bottom: 1px dashed #8b0000;
    }
    .stat-item:last-child { border-bottom: none; }
    .error-box {
        background-color: #1a0000;
        border: 3px solid #ff0000;
        padding: 30px;
        text-align: center;
        color: #ff3333;
    }
    .error-box h1 { font-size: 3em; }
    ul.feature-list { list-style: none; }
    ul.feature-list li {
        padding: 10px;
        margin: 8px 0;
        background-color: rgba(139, 0, 0, 0.2);
        border-left: 4px solid #ff0000;
    }
    /* Галерея */
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        margin-top: 20px;
    }
    .gallery-item {
        background-color: #1a0000;
        border: 2px solid #8b0000;
        padding: 15px;
        text-align: center;
        border-radius: 5px;
    }
    .gallery-item:hover { border-color: #ff0000; }
    .card-icon { font-size: 3em; margin-bottom: 10px; }
    /* Топ игроков */
    .player-row {
        display: flex;
        align-items: center;
        padding: 12px;
        border-bottom: 1px solid #8b0000;
    }
    .player-row:last-child { border-bottom: none; }
    .rank {
        font-size: 1.5em;
        font-weight: bold;
        color: #ff0000;
        width: 40px;
    }
    .player-info { flex: 1; }
    .player-trophies { color: #ff3333; font-weight: bold; }
</style>
'''

# ==================== Главн ====================
@app.route('/')
def home():
    return f'''
    <!DOCTYPE html>
    <html>
        <head><title>Главная</title>{CLASH_CSS}</head>
        <body>
            <div class="container">
                <h1>👑 CLASH ROYALE 👑</h1>
                <div class="battle-arena">
                    <p style="font-size: 1.2em;">Добро пожаловать на арену!</p>
                </div>
                <p>Сражайся, побеждай и становись легендой</p>
                <div class="nav-menu">
                    <a href="/game-info"📖 Об игре</a>
                    <a href="/gallery"> Галерея</a>
                    <a href="/top-players">🏆 Топ игроков</a>
                    <a href="/products"> Карты</a>
                    <a href="/contact"> Связь</a>
                </div>
            </div>
        </body>
    </html>
    '''

# ==================== Об игре ====================
@app.route('/game-info')
def game_info():
    return f'''
    <!DOCTYPE html>
    <html>
        <head><title>Об игре</title>{CLASH_CSS}</head>
        <body>
            <div class="container">
                <h1> ОБ ИГРЕ</h1>
                <div class="card">
                    <h2> Что такое Clash Royale?</h2>
                    <p>Clash Royale — это стратегия в реальном времени от создателей Clash of Clans.</p>
                    <p> <strong>Жанр:</strong> Карточная стратегия / Tower Defense</p>
                    <p> <strong>Игроки:</strong> 1vs1, 2vs2, клановые войны</p>
                    <p> <strong>Цель:</strong> Уничтожить башни противника за 3 минуты</p>
                </div>
                <div class="card">
                    <h2> Как играть?</h2>
                    <ul class="feature-list">
                        <li>Собери колоду из 8 карт</li>
                        <li>Трать эликсир на призыв войск</li>
                        <li>Защищай свои башни и атакуй врага</li>
                        <li>Побеждай и получай трофеи</li>
                    </ul>
                </div>
                <div class="nav-menu">
                    <a href="/">🏠 На главную</a>
                </div>
            </div>
        </body>
    </html>
    '''

# ==================== Галерея карт ====================
@app.route('/gallery')
def gallery():
    cards = [
        {"icon": "👹", "name": "P.E.K.K.A", "type": "Воин"},
        {"icon": "🐉", "name": "Дракон", "type": "Летающий"},
        {"icon": "⚡", "name": "Молния", "type": "Заклинание"},
        {"icon": "🏰", "name": "Башня", "type": "Здание"},
        {"icon": "💀", "name": "Скелеты", "type": "Армия"},
        {"icon": "🔥", "name": "Огненный шар", "type": "Заклинание"},
        {"icon": "🧙", "name": "Волшебник", "type": "Маг"},
        {"icon": "🛡️", "name": "Рыцарь", "type": "Воин"},
    ]
    
    html = f'''
    <!DOCTYPE html>
    <html>
        <head><title>Галерея</title>{CLASH_CSS}</head>
        <body>
            <div class="container">
                <h1> ГАЛЕРЕЯ КАРТ</h1>
                <div class="gallery-grid">
    '''
    
    for card in cards:
        html += f'''
                    <div class="gallery-item">
                        <div class="card-icon">{card["icon"]}</div>
                        <p class="gold-text">{card["name"]}</p>
                        <p style="font-size: 0.9em; color: #888;">{card["type"]}</p>
                    </div>
        '''
    
    html += f'''
                </div>
                <div class="nav-menu">
                    <a href="/">🏠 На главную</a>
                    <a href="/products"> Все карты</a>
                </div>
            </div>
        </body>
    </html>
    '''
    return html

# ==================== Топ игроков ====================
@app.route('/top-players')
def top_players():
    players = [
        {"rank": 1, "name": "ShadowKing", "trophies": "8,542", "clan": "🔥 ELITE 🔥"},
        {"rank": 2, "name": "DragonMaster", "trophies": "8,401", "clan": "⚡ Thunder ⚡"},
        {"rank": 3, "name": "PekkaLove", "trophies": "8,299", "clan": "👹 Beasts 👹"},
        {"rank": 4, "name": "WizardPro", "trophies": "8,156", "clan": "✨ Magic ✨"},
        {"rank": 5, "name": "TowerDefender", "trophies": "8,023", "clan": "🏰 Walls 🏰"},
        {"rank": 6, "name": "LightningFast", "trophies": "7,945", "clan": "⚡ Storm ⚡"},
        {"rank": 7, "name": "SkeletonArmy", "trophies": "7,821", "clan": "💀 Dead 💀"},
        {"rank": 8, "name": "FireBallKing", "trophies": "7,704", "clan": "🔥 Burn 🔥"},
    ]
    
    html = f'''
    <!DOCTYPE html>
    <html>
        <head><title>Топ игроков</title>{CLASH_CSS}</head>
        <body>
            <div class="container">
                <h1>🏆 ТОП ИГРОКОВ</h1>
                <div class="card">
    '''
    
    for player in players:
        medal = "🥇" if player["rank"] == 1 else "🥈" if player["rank"] == 2 else "🥉" if player["rank"] == 3 else "🔸"
        html += f'''
                    <div class="player-row">
                        <span class="rank">{medal} {player["rank"]}</span>
                        <div class="player-info">
                            <strong>{player["name"]}</strong><br>
                            <small style="color: #888;">{player["clan"]}</small>
                        </div>
                        <span class="player-trophies">🏆 {player["trophies"]}</span>
                    </div>
        '''
    
    html += f'''
                </div>
                <div class="nav-menu">
                    <a href="/">🏠 На главную</a>
                </div>
            </div>
        </body>
    </html>
    '''
    return html

# ==================== Карты  ====================
@app.route('/products')
def products():
    products_list = [
        {"id": 1, "name": "P.E.K.K.A", "price": 7, "desc": "Мощный воин с огромным уроном"},
        {"id": 2, "name": "Дракон", "price": 4, "desc": "Летающий юнит с уроном по области"},
        {"id": 3, "name": "Молния", "price": 6, "desc": "Заклинание: урон по 3 целям"},
    ]
    
    html = f'''
    <!DOCTYPE html>
    <html>
        <head><title>Карты</title>{CLASH_CSS}</head>
        <body>
            <div class="container">
                <h1>🃏 КАРТОЧКИ</h1>
    '''
    
    for product in products_list:
        html += f'''
                <div class="product-card">
                    <h2>{product["name"]}</h2>
                    <p>{product["desc"]}</p>
                    <div class="elixir-bar">
                        <div class="elixir-fill" style="width: {product["price"] * 14}%"></div>
                    </div>
                    <p class="gold-text">💜 {product["price"]} эликсира</p>
                    <a href="/product/{product["id"]}" class="btn">Подробнее</a>
                </div>
        '''
    
    html += f'''
                <div class="nav-menu">
                    <a href="/">🏠 На главную</a>
                    <a href="/gallery">🖼️ Галерея</a>
                </div>
            </div>
        </body>
    </html>
    '''
    return html

# ==================== Детали опер карты ====================
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    products = {
        1: {"name": "P.E.K.K.A", "price": 7, "description": "Мощный ближний боец", 
            "specs": "Урон: Высокий | Здоровье: Очень высокое | Скорость: Медленная"},
        2: {"name": "Дракон", "price": 4, "description": "Летающий юнит",
            "specs": "Урон: Средний | Здоровье: Среднее | Атака: По области"},
        3: {"name": "Молния", "price": 6, "description": "Заклинание",
            "specs": "Урон: Очень высокий | Цели: 3 | Радиус: Средний"},
    }
    
    if product_id in products:
        product = products[product_id]
        return f'''
        <!DOCTYPE html>
        <html>
            <head><title>{product["name"]}</title>{CLASH_CSS}</head>
            <body>
                <div class="container">
                    <h1>{product["name"]}</h1>
                    <div class="battle-arena">
                        <p style="font-size: 1.2em;">{product["description"]}</p>
                    </div>
                    <div class="stats-box">
                        <div class="stat-item"><span>💜 Эликсир:</span><span class="gold-text">{product["price"]}</span></div>
                        <div class="stat-item"><span>📋 Характеристики:</span><span>{product["specs"]}</span></div>
                    </div>
                    <button class="btn" style="width: 100%;">🃏 Добавить в колоду</button>
                    <div class="nav-menu">
                        <a href="/products">← Все карты</a>
                        <a href="/">🏠 На главную</a>
                    </div>
                </div>
            </body>
        </html>
        '''
    else:
        abort(404)

# ==================== Контакт ====================
@app.route('/contact')
def contact():
    return f'''
    <!DOCTYPE html>
    <html>
        <head><title>Контакты</title>{CLASH_CSS}</head>
        <body>
            <div class="container">
                <h1> СВЯЗЬ</h1>
                <div class="card">
                    <p><strong> Email:</strong> eferuj@gmail.com</p>
                    <p><strong> Dis:</strong> ClashRoyale6767</p>
                </div>
                <div class="card">
                    <h2>✉️ Написать</h2>
                    <form>
                        <input type="text" placeholder="Ваш ник">
                        <input type="gmail" placeholder="Gmail">
                        <input type="text" placeholder="Сообщение">
                        <button type="submit" class="btn">📤 Отправить</button>
                    </form>
                </div>
                <div class="nav-menu">
                    <a href="/">🏠 На главную</a>
                </div>
            </div>
        </body>
    </html>
    '''


@app.route('/api/data')
def api_data():
    data = {
        "status": "success",
        "arena": "Clash Royale",
        "items": [
            {"id": 1, "name": "P.E.K.K.A", "elixir": 7},
            {"id": 2, "name": "Dragon", "elixir": 4},
        ]
    }
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(error):
    return f'''
    <!DOCTYPE html>
    <html>
        <head><title>404</title>{CLASH_CSS}</head>
        <body>
            <div class="container">
                <div class="error-box">
                    <h1> 404 </h1>
                    <p>Арена не найдена!</p>
                </div>
                <div class="nav-menu" style="text-align: center; margin-top: 20px;">
                    <a href="/" style="display: inline-block;">🏠 На базу</a>
                </div>
            </div>
        </body>
    </html>
    ''', 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
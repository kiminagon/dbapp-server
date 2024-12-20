from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app)


@app.route('/publishers', methods=['GET'])
def get_publishers():
    
    connection = psycopg.connect(
    host='localhost',
    dbname='students',
    user='postgres',
    password='password',
    )
    result = connection.execute(sql)
    publishers = [
    {"出版社番号": row[0], "出版社名": row[1]}
        for row in result
    ]
    return jsonify(publishers)


@app.route('/publishers', methods=['POST'])
def post_publisher():
    content = request.get_json()
    print(content)
    return jsonify({'message': 'created'})


@app.route('/authors', methods=['GET'])
def get_authors():
    authors = [
        {'著者番号': 1,  '著者名': 'D. A. ノーマン'},
        {'著者番号': 2,  '著者名': '岡本明'},
        {'著者番号': 3,  '著者名': '安村通晃'},
        {'著者番号': 4,  '著者名': '伊賀聡一郎'},
        {'著者番号': 5,  '著者名': '野島久雄'},
        {'著者番号': 6,  '著者名': 'Robin Williams'},
        {'著者番号': 7,  '著者名': '米谷テツヤ'},
        {'著者番号': 8,  '著者名': '小原司'},
        {'著者番号': 9,  '著者名': '吉川典秀'},
        {'著者番号': 10, '著者名':  'David Kopec'},
        {'著者番号': 11, '著者名':  '黒川利明'},
        {'著者番号': 12, '著者名':  '日本大学文理学部'}
    ]
    return jsonify(authors)


@app.route('/authors', methods=['POST'])
def post_author():
    content = request.get_json()
    print(content)
    return jsonify({'message': 'created'})


@app.route('/books', methods=['GET'])
def get_books():
    books = [
        {
            'ISBNコード': '978-4788514348',
            '書籍名': '誰のためのデザイン？　増補・改訂版　―認知科学者のデザイン原論',
            '著者': [
                {'著者番号': 1, '著者名': 'D. A. ノーマン', '役割': '著'},
                {'著者番号': 2, '著者名': '岡本明', '役割': '翻訳'},
                {'著者番号': 3, '著者名': '安村通晃', '役割': '翻訳'},
                {'著者番号': 4, '著者名': '伊賀聡一郎', '役割': '翻訳'},
                {'著者番号': 5, '著者名': '野島久雄', '役割': '翻訳'},
            ],
            '出版社': {
                '出版社番号': 1,
                '出版社名': '新曜社'
            },
            '出版年': 2015
        },
        {
            'ISBNコード': '978-4839955557',
            '書籍名': 'ノンデザイナーズ・デザインブック [第4版]',
            '著者': [
                {'著者番号': 6, '著者名': 'Robin Williams', '役割': '著'},
                {'著者番号': 7, '著者名': '米谷テツヤ', '役割': '監修・翻訳'},
                {'著者番号': 8, '著者名': '小原司', '役割': '監修・翻訳'},
                {'著者番号': 9, '著者名': '吉川典秀', '役割': '翻訳'},
            ],
            '出版社': {
                '出版社番号': 2,
                '出版社名': 'マイナビ出版'
            },
            '出版年': 2016
        },
        {
            'ISBNコード': '978-4873118819',
            '書籍名': 'Python計算機科学新教本 ―新定番問題を解決する探索アルゴリズム、k平均法、ニューラルネットワーク',
            '著者': [
                {'著者番号': 10, '著者名': 'David Kopec', '役割': '著'},
                {'著者番号': 11, '著者名': '黒川利明', '役割': '翻訳'},
            ],
            '出版社': {
                '出版社番号': 3,
                '出版社名': 'オライリージャパン'
            },
            '出版年': 2019
        },
        {
            'ISBNコード': '978-4480069429',
            '書籍名': '知のスクランブル: 文理的思考の挑戦',
            '著者': [
                {'著者番号': 12, '著者名': '日本大学文理学部', '役割': '編集'},
            ],
            '出版社': {
                '出版社番号': 4,
                '出版社名': '筑摩書房'
            },
            '出版年': 2017
        }
    ]
    return jsonify(books)


@app.route('/books', methods=['POST'])
def post_book():
    content = request.get_json()
    print(content)
    return jsonify({'message': 'created'})


@app.route('/lendings', methods=['GET'])
def get_lendings():
    lendings = [
        {
            '貸出番号': 42,
            '貸出日': '2021-07-09',
            '返却予定日': '2021-07-23',
            '返却確認日': '2021-07-21',
            '書籍': [
                {
                    'ISBNコード': '978-4788514348',
                    '書籍名': '誰のためのデザイン？　増補・改訂版　―認知科学者のデザイン原論',
                    '著者': [
                        {'著者番号': 1, '著者名': 'D. A. ノーマン', '役割': '著'},
                        {'著者番号': 2, '著者名': '岡本明', '役割': '翻訳'},
                        {'著者番号': 3, '著者名': '安村通晃', '役割': '翻訳'},
                        {'著者番号': 4, '著者名': '伊賀聡一郎', '役割': '翻訳'},
                        {'著者番号': 5, '著者名': '野島久雄', '役割': '翻訳'},
                    ],
                    '出版社': {
                        '出版社番号': 1,
                        '出版社名': '新曜社'
                    },
                    '出版年': 2015
                },
                {
                    'ISBNコード': '978-4839955557',
                    '書籍名': 'ノンデザイナーズ・デザインブック [第4版]',
                    '著者': [
                        {'著者番号': 6, '著者名': 'Robin Williams', '役割': '著'},
                        {'著者番号': 7, '著者名': '米谷テツヤ', '役割': '監修・翻訳'},
                        {'著者番号': 8, '著者名': '小原司', '役割': '監修・翻訳'},
                        {'著者番号': 9, '著者名': '吉川典秀', '役割': '翻訳'},
                    ],
                    '出版社': {
                        '出版社番号': 2,
                        '出版社名': 'マイナビ出版'
                    },
                    '出版年': 2016
                },
            ],
            '学生': {
                '学生証番号': '5420365',
                '学生氏名': '矢吹紫',
            }
        },
        {
            '貸出番号': 43,
            '貸出日': '2021-09-03',
            '返却予定日': '2021-09-17',
            '返却確認日': None,
            '書籍': [
                {
                    'ISBNコード': '978-4873118819',
                    '書籍名': 'Python計算機科学新教本 ―新定番問題を解決する探索アルゴリズム、k平均法、ニューラルネットワーク',
                    '著者': [
                        {'著者番号': 10, '著者名': 'David Kopec', '役割': '著'},
                        {'著者番号': 11, '著者名': '黒川利明', '役割': '翻訳'},
                    ],
                    '出版社': {
                        '出版社番号': 3,
                        '出版社名': 'オライリージャパン'
                    },
                    '出版年': 2019
                },
            ],
            '学生': {
                '学生証番号': '5419513',
                '学生氏名': '高橋博之',
            }
        },
        {
            '貸出番号': 44,
            '貸出日': '2021-10-11',
            '返却予定日': '2021-10-25',
            '返却確認日': '2021-10-14',
            '書籍': [
                {
                    'ISBNコード': '978-4480069429',
                    '書籍名': '知のスクランブル: 文理的思考の挑戦',
                    '著者': [
                        {'著者番号': 12, '著者名': '日本大学文理学部', '役割': '編集'},
                    ],
                    '出版社': '筑摩書房',
                    '出版年': 2017
                }
            ],
            '学生': {
                '学生証番号': '6121M78',
                '学生氏名': '田中淳平'
            }
        }
    ]
    return jsonify(lendings)


@app.route('/lendings', methods=['POST'])
def post_lending():
    content = request.get_json()
    print(content)
    return jsonify({'message': 'created'})


@app.route('/lendings/<int:lending_id>/return', methods=['POST'])
def post_lending_return(lending_id):
    content = request.get_json()
    print(lending_id, content)
    return jsonify({'message': 'updated'})


@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {'学生証番号': '5420365', '学生氏名': '矢吹紫'},
        {'学生証番号': '5419513', '学生氏名': '高橋博之'},
        {'学生証番号': '6121M78', '学生氏名': '田中淳平'}
    ]
    return jsonify(users)


@app.route('/users', methods=['POST'])
def post_users():
    content = request.get_json()
    print(content)
    return jsonify({'message': 'created'})

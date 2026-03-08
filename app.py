from flask import Flask, render_template_string, request

app = Flask(__name__)

# Template HTML Utama
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Sistem Verifikasi Santri</title>
    <style>
        body { font-family: 'Courier New', Courier, monospace; text-align: center; margin-top: 100px; background: #1a1a1a; color: #0f0; }
        .box { border: 2px solid #0f0; padding: 30px; display: inline-block; border-radius: 10px; background: #000; }
        input { padding: 10px; border: 1px solid #0f0; background: #222; color: #0f0; border-radius: 5px; }
        button { padding: 10px 20px; background: #0f0; color: #000; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <div class="box">
        <h2>[ SHIELD SYSTEM v2.0 ]</h2>
        <p>IDENTIFIKASI DIRI ANDA:</p>
        <form method="POST">
            <input type="password" name="password" placeholder="Input Password..." required>
            <button type="submit">LOGIN</button>
        </form>
        {% if msg %}<p style="color: #0f0; margin-top: 20px;"><strong>{{ msg }}</strong></p>{% endif %}
    </div>
</body>
</html>
"""

# Halaman Ejekan sebelum mental ke Google
HTML_GOKIL = """
<!DOCTYPE html>
<html>
<head>
 
    <title>WKWKWK</title>
    <style>
        /* Efek Flicker (Kedip Monitor Jadul) */
        @keyframes flicker {
            0% { opacity: 0.9; }
            100% { opacity: 1; }
        }
        /* Efek Fade In-Out Angka */
        @keyframes scanline {
            0% { opacity: 0; transform: scale(0.8); }
            50% { opacity: 1; transform: scale(1); }
            100% { opacity: 0; transform: scale(1.2); }
        }
        body { 
            background-color: #0a0a0a; /* Hitam Monitor */
            color: #00ff00; /* Hijau Neon */
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
            overflow: hidden;
            animation: flicker 0.1s infinite; /* Efek getar monitor */
            text-shadow: 0 0 10px #00ff00; /* Tulisan Menyala */
        }
        img { 
            width: 200px; 
            filter: sepia(100%) hue-rotate(90deg) brightness(1.2); /* Paksa gambar jadi hijau */
            border: 2px solid #00ff00;
            padding: 5px;
            margin-bottom: 20px;
        }
        h1 { 
            font-size: 35px; 
            margin: 10px 0; 
            border: 1px solid #00ff00;
            padding: 10px;
            background: rgba(0, 255, 0, 0.1);
        }
        p { font-size: 18px; letter-spacing: 2px; }
        
        #counter { 
            font-size: 150px; 
            font-weight: bold; 
            color: #00ff00;
            animation: scanline 1s infinite;
        }
        /* Garis scanline monitor tua */
        body::before {
            content: " ";
            display: block;
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                        linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            z-index: 2;
            background-size: 100% 2px, 3px 100%;
            pointer-events: none;
        }
    </style>
    
</head>
<body>
     <img src="https://media.giphy.com/media/3o7TKsQ1208504928k/giphy.gif" alt="System Error">
    <h1>HAHAHA KAMU SALAH!</h1>
    <p>Sistem Dimasuki Malware </p>
    <P>KAMU AKAN TERHACK<p>
    <div id="counter">5</div>

    
      <script>
        let countdown = 5;
        const counterElement = document.getElementById('counter');

        const timer = setInterval(() => {
            countdown--;
            if (countdown > 0) {
                counterElement.textContent = countdown;
            } else {
                clearInterval(timer);
                window.location.href = "https://www.google.com";
            }
        }, 1000);
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ""
    if request.method == 'POST':
        user_input = request.form.get('password')
        
        if user_input == "aman":
            msg = "✅ AKSES DITERIMA. Selamat datang, Admin."
            return render_template_string(HTML_FORM, msg=msg)
        else:
            # Jika salah, tampilkan halaman ejekan
            return render_template_string(HTML_GOKIL)
            
    return render_template_string(HTML_FORM, msg=msg)

# Persiapan buat Vercel
app = app

if __name__ == '__main__':
    app.run(debug=True)

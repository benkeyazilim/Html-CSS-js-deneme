<?php
// Yorumların kaydedileceği dosya
$yorumlar_dosyasi = 'yorumlar.txt';

// Form gönderildi mi kontrol et
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $ad = isset($_POST['ad']) ? htmlspecialchars($_POST['ad']) : 'Anonim';
    $yorum = isset($_POST['yorum']) ? htmlspecialchars($_POST['yorum']) : '';

    if (!empty($yorum)) {
        // Yorumu ve zamanı birleştir
        $yeni_yorum = "[" . date('Y-m-d H:i:s') . "] " . $ad . ": " . $yorum . "\n";

        // Yorumu dosyaya ekle (append)
        file_put_contents($yorumlar_dosyasi, $yeni_yorum, FILE_APPEND | LOCK_EX);

        // Sayfayı yenileyerek formun tekrar gönderilmesini engelle
        header('Location: yorum-yap.php');
        exit;
    }
}

// Dosyadan mevcut yorumları oku
$yorumlar = file_exists($yorumlar_dosyasi) ? file($yorumlar_dosyasi, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) : [];
?>
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Yorum Yap</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        body { font-family: 'Poppins', sans-serif; background-color: #f4f4f9; color: #333; text-align: center; }
        .comment-page-container { max-width: 600px; margin: 50px auto; padding: 40px; background-color: #fff; border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); }
        h1 { color: #0033cc; }
        form { display: flex; flex-direction: column; gap: 20px; margin-bottom: 40px; }
        input, textarea { padding: 12px; border-radius: 5px; border: 1px solid #ccc; font-family: 'Poppins', sans-serif; }
        button { padding: 15px; background-color: #e67e22; color: white; border: none; border-radius: 50px; cursor: pointer; font-size: 1em; font-weight: bold; transition: background-color 0.3s; }
        button:hover { background-color: #d35400; }
        .comments-section { text-align: left; }
        .comments-section h2 { color: #0033cc; border-bottom: 2px solid #ffcc00; padding-bottom: 10px; margin-bottom: 20px; }
        .comment { border-bottom: 1px solid #eee; padding: 15px 0; }
        .comment:last-child { border-bottom: none; }
        .comment-meta { font-size: 0.9em; color: #777; margin-bottom: 5px; }
        .comment-text { font-size: 1em; }
    </style>
</head>
<body>

<div class="comment-page-container">
    <a href="menü-deneme.html" style="float: left; text-decoration: none; color: #0033cc; font-size: 1.2em;">&larr; Menüye Geri Dön</a>
    <h1>Yorumunu Bırak</h1>
    
    <form method="POST" action="yorum-yap.php">
        <input type="text" name="ad" placeholder="Adınız Soyadınız">
        <textarea name="yorum" rows="5" placeholder="Yorumunuzu buraya yazın..."></textarea>
        <button type="submit">Yorumu Gönder</button>
    </form>

    <div class="comments-section">
        <h2>Yorumlar</h2>
        <?php
        // Yorumları tersten sıralayarak en yeniyi en üste getir
        $yorumlar = array_reverse($yorumlar);
        foreach ($yorumlar as $yorum_satiri) {
            echo "<div class='comment'><div class='comment-text'>" . htmlspecialchars($yorum_satiri) . "</div></div>";
        }
        if (empty($yorumlar)) {
            echo "<p>Henüz yorum yapılmadı.</p>";
        }
        ?>
    </div>
</div>

</body>
</html>
import pytest
import os
# Dosya adınla birebir uyumlu import:
from src.bot_detection_analyzer import SystemHealthChecker, BotDetectionAnalyzer

# 🛠️ SystemHealthChecker (Self-Check) Testleri
def test_health_checker_status():
    """Yönergedeki 'Auto Test Ability' mekanizmasını doğrular"""
    checker = SystemHealthChecker()
    # Başlangıçta hata listesi boş olmalı
    assert len(checker.errors) == 0

def test_directory_logic():
    """Klasör oluşturma mantığının doğruluğunu test eder"""
    checker = SystemHealthChecker()
    # assets/bot_analysis klasörünü kontrol eder
    status = checker.check_directory_structure()
    assert status is True
    assert os.path.exists("assets/bot_analysis")

# 🤖 BotDetectionAnalyzer Testleri
def test_analyzer_stealth_check():
    """Analyzer'ın stealth modunun aktifliğini test eder"""
    analyzer = BotDetectionAnalyzer(stealth_mode=True)
    assert analyzer.stealth_mode is True

def test_risk_scoring_calculation():
    """Risk puanlama algoritmasının siber güvenlik mantığını test eder"""
    analyzer = BotDetectionAnalyzer()
    
    # Mock (Sahte) veri: WebDriver tespit edildi (+3 puan)
    mock_data = {
        'webdriver': {'present': True},
        'automation': {'selenium': False},
        'plugins': {'count': 5},
        'hardware': {'hardwareConcurrency': 4, 'maxTouchPoints': 1},
        'canvas': 'valid_hash'
    }
    score = analyzer.calculate_risk_score(mock_data)
    # Skorun 3 olduğundan emin olalım
    assert score == 3

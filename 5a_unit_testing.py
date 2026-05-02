import unittest

from EmotionDetection.emotion_detection import format_emotion_detector

class TestEmotionDetectionAnalyzer(unittest.TestCase):
    def test_emotion_detection_1(self):
        result_1 = format_emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")

    def test_emotion_detection_2(self):   
        result_2 = format_emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")
    
    def test_emotion_detection_3(self):
        result_3 = format_emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")

    def test_emotion_detection_4(self):    
        result_4 = format_emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")

    def test_emotion_detection_5(self):    
        result_5 = format_emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "fear")

if __name__ == '__main__':
    unittest.main()
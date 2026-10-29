'''
Unit tests for the emotion_detector function.
Tests dominant emotion detection for all five emotions.
'''
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


def make_mock_response(emotion_scores, status_code=200):
    '''Helper to build a mock requests.Response object.'''
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.json.return_value = {
        "emotionPredictions": [{"emotion": emotion_scores}]
    }
    return mock_resp


class TestEmotionDetector(unittest.TestCase):
    '''Test cases for the emotion_detector function.'''

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_emotion(self, mock_post):
        '''Test that joy is the dominant emotion for a happy statement.'''
        mock_post.return_value = make_mock_response(
            {'anger': 0.006, 'disgust': 0.002, 'fear': 0.005,
             'joy': 0.964, 'sadness': 0.023}
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_emotion(self, mock_post):
        '''Test that anger is the dominant emotion for an angry statement.'''
        mock_post.return_value = make_mock_response(
            {'anger': 0.861, 'disgust': 0.076, 'fear': 0.034,
             'joy': 0.007, 'sadness': 0.022}
        )
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_emotion(self, mock_post):
        '''Test that disgust is the dominant emotion.'''
        mock_post.return_value = make_mock_response(
            {'anger': 0.107, 'disgust': 0.802, 'fear': 0.020,
             'joy': 0.005, 'sadness': 0.066}
        )
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_emotion(self, mock_post):
        '''Test that sadness is the dominant emotion.'''
        mock_post.return_value = make_mock_response(
            {'anger': 0.050, 'disgust': 0.011, 'fear': 0.035,
             'joy': 0.029, 'sadness': 0.875}
        )
        result = emotion_detector("It is really sad this happened")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_emotion(self, mock_post):
        '''Test that fear is the dominant emotion.'''
        mock_post.return_value = make_mock_response(
            {'anger': 0.052, 'disgust': 0.012, 'fear': 0.831,
             'joy': 0.012, 'sadness': 0.093}
        )
        result = emotion_detector("I am scared to death by this")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()

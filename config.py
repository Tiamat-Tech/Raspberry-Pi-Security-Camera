from __future__ import print_function
import secret
import cv2


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(object):
    __metaclass__ = Singleton

    live_preview_with_detection = False
    send_email_notifications = False

    classifierNameLocationDict = {
        'motion_detector': {'description': 'Motion detector'},

        # Face
        'face_detection': {'description': 'Face detection (haarcascade)',
                           'location': 'models/haar/haarcascade_frontalface_default.xml'},
        'lbpcascade_frontalface_improved': {'description': 'Face detection (lbp)',
                                            'location': 'models/lbp/lbpcascade_frontalface_improved.xml'},

        # Haar
        'full_body_detection': {'description': 'Full body detection',
                                'location': 'models/haar/haarcascade_fullbody.xml'},
        'haarcascade_upperbody': {'description': 'Upper body detection',
                                  'location': 'models/haar/haarcascade_upperbody.xml'},
        'haarcascade_smile': {'description': 'Smile detection',
                              'location': 'models/haar/haarcascade_smile.xml'},

        # lbp
        'lbpcascade_frontalcatface': {'description': 'Cat face detection',
                                      'location': 'models/lbp/lbpcascade_frontalcatface.xml'},
        'lbpcascade_silverware': {'description': 'Silverware detection',
                                                     'location': 'models/lbp/lbpcascade_silverware.xml'}
    }

    classifier_name = 'motion_detector'
    classifier = None
    classifier2 = None


    def to_string(self):
        attributes = vars(self)
        print(self.__class__.__name__ + ' attributes: ')
        print(', '.join("%s: %s" % item for item in attributes.items()))
        print(self.__dict__)

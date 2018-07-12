"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "1. Basics": [
        {"input": ('bbw', 3),
         "answer": 0.48,
         "explanation": 0.481},

        {"input": ('wwb', 3),
         "answer": 0.52,
         "explanation": 0.519},

        {"input": ('www', 3),
         "answer": 0.56,
         "explanation": 0.556},

        {"input": ('bbbb', 1),
         "answer": 0.0,
         "explanation": 0.0},

        {"input": ('wwbb', 4),
         "answer": 0.5,
         "explanation": 0.5},

        {"input": ('bwbwbwb', 5),
         "answer": 0.48,
         "explanation": 0.481},
    ],
    "2. Extra": [
        {"input": ('bwwbbbbw', 4),
         "answer": 0.45,
         "explanation": 0.447},

        {"input": ('bbb', 5),
         "answer": 0.49,
         "explanation": 0.494},

        {"input": ('bwbwbb', 4),
         "answer": 0.45,
         "explanation": 0.451},

        {"input": ('wbbb', 3),
         "answer": 0.44,
         "explanation": 0.438},

        {"input": ('wwbbwbwbwb', 2),
         "answer": 0.5,
         "explanation": 0.5},

        {"input": ('wbwwwww', 2),
         "answer": 0.76,
         "explanation": 0.755},

        {"input": ('wbwwwwwwwb', 4),
         "answer": 0.65,
         "explanation": 0.654},

        {"input": ('bwb', 2),
         "answer": 0.44,
         "explanation": 0.444},

        {"input": ('bbbbw', 5),
         "answer": 0.46,
         "explanation": 0.461},

        {"input": ('wbwwwwwb', 3),
         "answer": 0.64,
         "explanation": 0.641},
    ],
    "3. Weird": [
        {"input": ('w', 1),
         "answer": 1.0,
         "explanation": 1.0},

        {"input": ('b', 1),
         "answer": 0.0,
         "explanation": 0.0},

        {"input": ('w', 2),
         "answer": 0.0,
         "explanation": 0.0},

        {"input": ('b', 2),
         "answer": 1.0,
         "explanation": 1.0},

        {"input": ('wwwwwwwwwwww', 4),
         "answer": 0.79,
         "explanation": 0.789},

        {"input": ('bbbbbbbbbbbb', 5),
         "answer": 0.26,
         "explanation": 0.259},

        {"input": ('wwwwwwwwwwwwwwwwwwww', 20),
         "answer": 0.57,
         "explanation": 0.567},
        
        {"input": ('bbbbbbbbbbbbbbbbbbbb', 20),
         "answer": 0.43,
         "explanation": 0.432},


    ],
    "4. Extra": [
        {"input": ('wwwwwbwbwbbwbbwwbw', 11),
         "answer": 0.53,
         "explanation": 0.534},

        {"input": ('wwbwwwbbwbbwww', 10),
         "answer": 0.54,
         "explanation": 0.536},

        {"input": ('bbwbwbbwbwwbw', 11),
         "answer": 0.49,
         "explanation": 0.493},
    ]

}

import pickle


class LanguageChecker:
    def __init__(self, automaton_path_dictionary: dict):
        self.automaton_path_dictionary = automaton_path_dictionary
        
    def _load_automaton(self, path_to_automaton: str):
        with open(path_to_automaton, "rb") as input_file:
            automaton = pickle.load(input_file)
        return automaton
    
    def filter_words(self, a_string_to_check: str, a_language: str):
        assert a_language in self.automaton_path_dictionary.keys(), 'no automaton is available in this language.'
        path_to_automaton = self.automaton_path_dictionary[a_language]
        automaton = self._load_automaton(path_to_automaton)
        normalized_string = self._string_normalization(a_string_to_check)
        words_to_keep = []
        for _, (_, original_value) in automaton.iter(normalized_string):
            splitted_normalized_string = normalized_string.split()
            if original_value in splitted_normalized_string:
                words_to_keep.append(original_value)
        return words_to_keep
    
    def is_language(self, a_string_to_check: str, a_language: str):
        normalized_string = self._string_normalization(a_string_to_check)
        words_to_keep = self.filter_words(normalized_string, a_language)
        if len(words_to_keep) > 1:
            return True
        else:
            return False
    
    def is_one_language(self, a_string_to_check: str, a_language: str):
        normalized_string = self._string_normalization(a_string_to_check)
        words_to_keep = self.filter_words(normalized_string, a_language)
        if len(words_to_keep) == len(normalized_string.split(' ')):
            return True
        else:
            return False
    
    @staticmethod
    def _string_normalization(a_string_to_check: str):
        normalization = filter(lambda x: x.isalnum() or x.isspace(), a_string_to_check)
        normalized_string = "".join(normalization).lower()
        normalized_string = " ".join(normalized_string.split())
        return normalized_string
        
        
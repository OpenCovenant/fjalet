def is_free_of_standalone_deletions():
    with open('./te-padeshiruarat.txt', 'rb') as deletions_file:
        deletions = deletions_file.readlines()
        with open('./fjalet.txt') as standalones_files:
            standalones = standalones_files.readlines()

            for deletion in deletions:
                if deletion in standalones:
                    raise ValueError(f'Fjala e padëshiruar {deletion} qenka shtuar te fjalet.txt')


is_free_of_standalone_deletions()

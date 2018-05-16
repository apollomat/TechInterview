# a play can lead to 2 points, 3 points, or 7
# # for example, four different combinations yield 12
#
#
#
# write a problem that takes a final score and scorse for individual plays and
# returns the number of possible combinations


def max_comb(final_score_value, play_scores):
    arr = [[1] + [0] * final_score_value for _ in play_scores] # 3 len(values), 12 (scores) in each
    for indx in range(len(play_scores)):
        for score in range(1, final_score_value + 1):
            point_value = play_scores[indx]
            prev_point_indx = indx - 1

            scores_with_value, scores_without_value = 0, 0
            if indx > 0:
                scores_without_value = arr[prev_point_indx][score]

            scores_with_value = 0
            if point_value <= score:
                scores_with_value = arr[indx][score - point_value]

            arr[indx][score] = scores_with_value + scores_without_value
    print arr
    return arr[len(play_scores) - 1][final_score_value]

print max_comb(12, [2,3,7])

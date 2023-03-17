import os, random, json

info_dict = {
    "names": [
        "Purple Haze", "Sour Diesel", "Blue Dream", "Girl Scout Cookies", "White Widow",
        "OG Kush", "Granddaddy Purple", "Green Crack", "Northern Lights", "Gorilla Glue",
        "Jack Herer", "AK-47", "Super Silver Haze", "Durban Poison", "Cherry Pie",
        "Blueberry Kush", "Lemon Haze", "Watermelon Zkittlez", "Pineapple Express", 
        "Gorilla Glue", "Jack Herer", "Sour Diesel", "OG Kush", "Strawberry Cough", 
        "Northern Lights", "Chemdawg", "Gelato", "White Widow", "Girl Scout Cookies", 
        "Maui Wowie", "Apple Fritter", "Alien OG", "Lemon Cake", "Mendo Breath", 
        "Tangerine Dream", "Banana Kush", "Purple Punch", "Gelato Cake", "Mimosa", 
        "Blackberry Kush", "Headband", "Platinum OG", "Strawberry Banana", "Lemon Kush",
        "Cherry AK-47", "Sherbert", "Purple Urkle", "Orange Creamsicle", "Blue Raspberry", 
        "Strawberry Cheesecake"
    ],
    "descriptions": [
        "This classic strain has a sweet, fruity aroma with hints of earthy undertones. It delivers a happy, uplifting, and energetic high that’s perfect for daytime use.",
        "Sour Diesel has a diesel-like aroma with a hint of citrus. Its high is cerebral, uplifting, and energizing, making it a great choice for getting things done.",
        "Blue Dream has a sweet, fruity aroma and a balanced high that combines a relaxed body buzz with an energizing and creative mental high.",
        "Girl Scout Cookies has a sweet, earthy aroma and a powerful high that combines a cerebral buzz with a full-body relaxation. It's perfect for evening use.",
        "White Widow has a floral, earthy aroma with a hint of sweetness. Its high is energetic and uplifting, making it a great choice for daytime use.",
        "OG Kush has a spicy, earthy aroma and a strong, relaxing high that can help alleviate stress, anxiety, and pain.",
        "Granddaddy Purple has a sweet, grape-like aroma and a strong, relaxing high that can help with insomnia, anxiety, and stress.",
        "Green Crack has a citrusy, fruity aroma and a strong, energizing high that can help with fatigue and depression.",
        "Northern Lights has a spicy, earthy aroma and a relaxing, full-body high that can help with insomnia, pain, and anxiety.",
        "Gorilla Glue has a pungent, earthy aroma and a strong, sedating high that can help with pain, insomnia, and stress.",
        "Jack Herer has a spicy, piney aroma and a euphoric, energizing high that can help with depression, fatigue, and stress.",
        "AK-47 has a sweet, floral aroma and a cerebral, uplifting high that can help with depression, anxiety, and pain.",
        "Super Silver Haze has a spicy, earthy aroma and a cerebral, energetic high that can help with fatigue and depression.",
        "Durban Poison has a sweet, earthy aroma and a cerebral, uplifting high that can help with depression, fatigue, and stress.",
        "Cherry Pie has a sweet, fruity aroma and a relaxing, full-body high that can help with pain, insomnia, and anxiety.",
        
        "Enjoy a sweet and fruity flavor with this indica-dominant strain. With a calming and relaxing effect, it's perfect for unwinding at the end of a long day. May relieve stress and anxiety.",
        "This sativa-dominant strain offers a refreshing and citrusy flavor. With an energetic and uplifting effect, it's great for starting your day off on the right foot. May relieve fatigue and depression.",
        "A balanced hybrid with a fruity and refreshing taste. Known for its euphoric and uplifting effects, it's a great choice for socializing with friends. May relieve pain and anxiety.",
        "This sativa-dominant strain offers a tropical and sweet flavor. With a creative and energetic effect, it's perfect for sparking inspiration and getting things done. May relieve stress and depression.",
        "An indica-dominant strain with a pungent and earthy taste. Known for its relaxing and sedative effects, it's perfect for winding down at the end of the day. May relieve pain and insomnia.",
        "This sativa-dominant strain offers a spicy and earthy flavor. With an energetic and uplifting effect, it's perfect for enhancing creativity and productivity. May relieve anxiety and depression.",
        "A popular sativa-dominant strain with a diesel-like aroma. Known for its cerebral and energizing effects, it's great for starting your day off with a boost. May relieve stress and pain.",
        "An indica-dominant strain with an earthy and piney taste. Known for its relaxing and euphoric effects, it's perfect for winding down after a long day. May relieve anxiety and insomnia.",
        "A sativa-dominant strain with a sweet and berry-like taste. With a creative and energetic effect, it's perfect for enhancing social interactions and sparking inspiration. May relieve stress and depression.",
        "An indica-dominant strain with a sweet and earthy taste. Known for its relaxing and sedative effects, it's perfect for winding down before bedtime. May relieve pain and insomnia.",
        "A hybrid strain with a pungent and diesel-like aroma. With a cerebral and euphoric effect, it's perfect for enhancing creativity and productivity. May relieve stress and anxiety.",
        "A balanced hybrid with a sweet and fruity flavor. Known for its relaxing and euphoric effects, it's perfect for unwinding after a long day. May relieve pain and anxiety.",
        "A balanced hybrid with an earthy and woody taste. Known for its cerebral and uplifting effects, it's great for sparking creativity and enhancing social interactions. May relieve stress and depression.",
        "A hybrid strain with a sweet and earthy flavor. With a creative and uplifting effect, it's perfect for enhancing focus and productivity. May relieve anxiety and depression.",
        "A sativa-dominant strain with a tropical and fruity taste. Known for its energetic and uplifting effects, it's great for starting your day off on the right foot. May relieve stress and fatigue.",

        "A hybrid strain with a sweet and cinnamon-like flavor. Known for its calming and relaxing effects, it's great for unwinding after a long day. May relieve anxiety and pain.",
        "An indica-dominant strain with a spicy and earthy taste. Known for its sedative and relaxing effects, it's perfect for winding down before bedtime. May relieve insomnia and pain.",
        "A sativa-dominant strain with a sweet and citrusy flavor. With an energetic and uplifting effect, it's perfect for enhancing creativity and productivity. May relieve stress and depression.",
        "An indica-dominant strain with a sweet and earthy taste. Known for its relaxing and sedative effects, it's perfect for unwinding at the end of the day. May relieve pain and anxiety.",
        "A sativa-dominant strain with a citrusy and tangy taste. Known for its energetic and uplifting effects, it's great for starting your day off on the right foot. May relieve depression and fatigue.",
        "An indica-dominant strain with a sweet and tropical flavor. Known for its relaxing and euphoric effects, it's perfect for winding down after a long day. May relieve pain and anxiety.",
        "A hybrid strain with a fruity and grape-like flavor. Known for its relaxing and sedative effects, it's perfect for unwinding before bedtime. May relieve stress and pain.",
        "A hybrid strain with a sweet and creamy flavor. With a calming and relaxing effect, it's perfect for unwinding after a long day. May relieve anxiety and depression.",
        "A sativa-dominant strain with a sweet and fruity flavor. Known for its energetic and uplifting effects, it's great for enhancing social interactions. May relieve stress and anxiety.",
        "An indica-dominant strain with a sweet and berry-like taste. Known for its relaxing and sedative effects, it's perfect for winding down at the end of the day. May relieve pain and insomnia.",
        "A hybrid strain with a diesel-like aroma. Known for its cerebral and euphoric effects, it's perfect for enhancing creativity and focus. May relieve stress and anxiety.",
        "An indica-dominant strain with a earthy and piney taste. Known for its relaxing and sedative effects, it's perfect for unwinding before bedtime. May relieve pain and insomnia.",
        "A balanced hybrid with a sweet and fruity flavor. With a calming and relaxing effect, it's perfect for unwinding after a long day. May relieve anxiety and pain.",
        "A hybrid strain with a citrusy and earthy taste. Known for its uplifting and energetic effects, it's perfect for starting your day off on the right foot. May relieve depression and fatigue.",
        "A sativa-dominant strain with a sweet and cherry-like flavor. With a creative and uplifting effect, it's perfect for sparking inspiration and productivity. May relieve stress and anxiety.",
        "A hybrid strain with a sweet and creamy flavor. Known for its relaxing and euphoric effects, it's perfect for unwinding at the end of the day. May relieve anxiety and pain.",
        "An indica-dominant strain with a sweet and grape-like flavor. Known for its sedative and relaxing effects, it's perfect for unwinding before bedtime. May relieve pain and insomnia."

        " A hybrid strain with a sweet and creamy flavor, reminiscent of the classic popsicle. Known for its calming and uplifting effects, it's great for relaxing with friends. May relieve stress and anxiety.",
        "A sativa-dominant strain with a tangy and fruity flavor, similar to the popular candy. With an energetic and creative effect, it's perfect for sparking inspiration and motivation. May relieve depression and fatigue.",
        "A balanced hybrid with a sweet and creamy flavor, reminiscent of the classic dessert. With a calming and uplifting effect, it's perfect for unwinding after a long day. May relieve pain and anxiety",
        "Introducing this premium strain, a sativa-dominant hybrid that is sure to elevate your experience. Known for its sweet, berry-like aroma and balanced effects, This strain offers a relaxed and uplifting high that is perfect for any occasion."
    ],
    "categories": [1, 2, 3, 4, 5, 6, 7, 8],
    # "categories": [
    #     "Edibles", "Pre-rolls", "Hybrids", "Concentrates", "Tropicals", "Mushrooms", "Flowers", "Accessories", "Edibles", "Flowers", "Pre-rolls", "Concentrates", "Tropicals", "Hybrids", "Accessories", "Mushrooms", "Flowers", "Pre-rolls", "Hybrids", "Concentrates", "Tropicals", "Accessories", "Mushrooms", "Flowers", "Pre-rolls", "Hybrids", "Concentrates", "Tropicals", "Accessories", "Mushrooms", "Flowers", "Pre-rolls", "Hybrids", "Concentrates", "Tropicals", "Accessories", "Mushrooms", "Flowers", "Pre-rolls", "Hybrids", "Concentrates", "Tropicals", "Accessories", "Mushrooms", "Flowers", "Pre-rolls", "Hybrids", "Concentrates", "Tropicals", "Accessories", "Mushrooms", "Flowers", "Pre-rolls", "Hybrids", "Concentrates", "Tropicals", "Accessories", "Mushrooms", "Flowers", "Pre-rolls"
    # ],
    "prices": [22.99, 17.00, 50.49, 64.42, 180.44, 31.43, 22.48, 21.86, 21.9, 43.32, 5.33, 58.33, 22.66, 20.71, 8.95, 20.99, 29.72, 7.32, 24.91, 169.99, 29.76, 11.86, 21.76, 23.09, 143.35, 185.75, 69.54, 13.74, 199.49, 330.00, 117.99, 8.14, 44.55, 45.99, 39.46, 16.55, 18.79, 29.85, 19.50, 30.99, 68.00, 12.45, 26.77, 15.38, 188.99, 141.00, 31.77, 26.00, 30.30, 44.00],
    "previous_prices": [24.99, 0, 54.99, 75.99, 199.99, 0, 24.99, 22.99, 23.99, 49.99, 0, 69.99, 24.99, 21.99, 0, 22.99, 32.99, 0, 27.99, 229.99, 32.99, 0, 23.99, 24.99, 159.99, 0, 79.99, 16.99, 249.99, 399.99, 0, 10.99, 49.99, 51.99, 44.99, 0, 21.99, 34.99, 23.99, 39.99, 89.99, 0, 29.99, 17.99, 219.99, 159.99, 34.99, 27.99, 32.99, 49.99],
    "effects": [
        ["Relaxation", "Happiness", "Euphoria", "Creativity", "Appetite stimulation"],
        ["Pain relief", "Relaxation", "Euphoria", "Appetite stimulation", "Sleepiness"],
        ["Euphoria", "Relaxation", "Upliftedness", "Happiness", "Creativity", "Appetite stimulation"],
        ["Psychedelic experience", "Euphoria", "Relaxation", "Spiritual awakening"],
        ["Relaxation", "Euphoria", "Upliftedness", "Happiness", "Creativity"],
        ["Relaxation", "Euphoria", "Hunger", "Sociability", "Giggles"],
        ["Relaxation", "Upliftedness", "Euphoria", "Happiness", "Creativity", "Focus"],
        ["Relaxation", "Upliftedness", "Euphoria", "Happiness", "Focus", "Sleepiness"],
        ["Upliftedness", "Happiness", "Euphoria", "Energy boost", "Creativity"],
        ["Relaxation", "Euphoria", "Happiness", "Pain relief", "Appetite stimulation"],
        ["Relaxation", "Euphoria", "Happiness", "Giggles"],
        ["Relaxation", "Euphoria", "Happiness", "Appetite stimulation", "Giggles"],
        ["Relaxation", "Euphoria", "Happiness", "Appetite stimulation", "Sleepiness"],
        ["Relaxation", "Euphoria", "Happiness", "Sleepiness", "Appetite stimulation"],
        ["Relaxation", "Euphoria", "Happiness", "Upliftedness", "Sleepiness", "Pain relief"],
        ["Upliftedness", "Happiness", "Euphoria", "Relaxation", "Creativity"],
        ["Relaxation", "Happiness", "Euphoria", "Appetite stimulation"],
        ["Pain relief", "Relaxation", "Euphoria", "Sleepiness"],
        ["Euphoria", "Relaxation", "Upliftedness", "Happiness", "Creativity"],
        ["Psychedelic experience", "Euphoria", "Relaxation", "Spiritual awakening"],
        ["Relaxation", "Euphoria", "Upliftedness", "Happiness", "Creativity"],
        ["Relaxation", "Euphoria", "Hunger", "Sociability", "Giggles"],
        ["Relaxation", "Upliftedness", "Euphoria", "Happiness", "Creativity", "Focus"],
        ["Relaxation", "Upliftedness", "Euphoria", "Happiness", "Focus", "Sleepiness"],
        ["Upliftedness", "Happiness", "Euphoria", "Energy boost", "Creativity"],
        ["Relaxation", "Euphoria", "Happiness", "Pain relief", "Appetite stimulation"],
        # ["Relaxation", "Euphoria", "Happiness", "Giggles"],
        ["Relaxation", "Euphoria", "Happiness", "Appetite stimulation", "Giggles"],
        ["Relaxation", "Euphoria", "Happiness", "Appetite stimulation", "Sleepiness"],
        ["Relaxation", "Euphoria", "Happiness", "Sleepiness", "Appetite stimulation"],
        ["Mental clarity", "Euphoria", "Upliftedness", "Happiness", "Energy boost"],
        ["Relaxation", "Happiness", "Appetite suppression", "Focus", "Productivity"],
        ["Euphoria", "Relaxation", "Upliftedness", "Happiness", "Giggles"],
        ["Mental stimulation", "Upliftedness", "Euphoria", "Creativity", "Sociability"],
        ["Relaxation", "Euphoria", "Hunger", "Sociability", "Giggles", "Creativity"],
        ["Relaxation", "Upliftedness", "Euphoria", "Happiness", "Focus"],
        ["Euphoria", "Happiness", "Mental stimulation", "Upliftedness", "Sociability"],
        ["Pain relief", "Relaxation", "Euphoria", "Happiness", "Giggles"],
        ["Euphoria", "Relaxation", "Upliftedness", "Happiness", "Productivity"],
        ["Relaxation", "Euphoria", "Happiness", "Giggles", "Appetite stimulation"],
        ["Mental stimulation", "Euphoria", "Upliftedness", "Happiness", "Creativity"],
        ["Relaxation", "Euphoria", "Upliftedness", "Happiness", "Productivity"],
        ["Euphoria", "Creativity", "Focus", "Motivation", "Energy boost", "Productivity"],
        ["Pain relief", "Relaxation", "Hunger", "Appetite suppression", "Giggles"],
        ["Upliftedness", "Happiness", "Euphoria", "Relaxation", "Sociability", "Anti-anxiety"],
        ["Psychedelic experience", "Euphoria", "Relaxation", "Spiritual awakening", "Deep introspection"],
        ["Relaxation", "Euphoria", "Happiness", "Sociability", "Giggles", "Sleepiness"],
        ["Euphoria", "Motivation", "Focus", "Productivity", "Anti-depressant"],
        ["Relaxation", "Upliftedness", "Euphoria", "Happiness", "Appetite stimulation", "Sexual arousal"],
        ["Pain relief", "Relaxation", "Euphoria", "Sleepiness", "Appetite stimulation", "Anti-inflammatory"],
        ["Upliftedness", "Happiness", "Euphoria", "Energy boost", "Creativity", "Focus", "Motivation"]
    ],
    "may_relieve": [
        ["Stress", "Depression", "Insomnia", "Anxiety", "Chronic pain", "Headaches", "Migraines", "Inflammation", "Nausea"],
        ["Chronic pain", "Insomnia", "Stress", "Depression", "Anxiety", "Muscle spasms", "Headaches", "Migraines", "Nausea", "Loss of appetite"],
        ["Depression", "Anxiety", "Stress", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Muscle spasms", "Insomnia"],
        # ["Depression", "Anxiety", "Stress", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea"],
        ["Depression", "Stress", "Anxiety", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Fatigue"],
        ["Depression", "Stress", "Anxiety", "Chronic pain", "Muscle spasms", "Nausea", "Loss of appetite", "Fatigue"],
        ["Depression", "Anxiety", "Stress", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Muscle spasms"],
        ["Insomnia", "Depression", "Stress", "Anxiety", "Chronic pain", "Headaches", "Migraines", "Inflammation", "Nausea", "Muscle spasms", "Fatigue"],
        ["Depression", "Anxiety", "Stress", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Muscle spasms"],
        ["Depression", "Anxiety", "Stress", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Muscle spasms", "Insomnia", "Fatigue"],
        ["Depression", "Stress", "Anxiety", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Fatigue"],
        ["Depression", "Stress", "Anxiety", "Chronic pain", "Muscle spasms", "Nausea", "Loss of appetite", "Fatigue"],
        ["Depression", "Anxiety", "Stress", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Muscle spasms"],
        ["Insomnia", "Depression", "Stress", "Anxiety", "Chronic pain", "Headaches", "Migraines", "Inflammation", "Nausea", "Muscle spasms", "Fatigue"],
        ["Depression", "Anxiety", "Stress", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Muscle spasms"],
        ["Depression", "Stress", "Anxiety", "Chronic pain", "Inflammation", "Headaches", "Migraines", "Nausea", "Fatigue"],
        ["Chronic pain", "Insomnia", "Stress", "Depression", "Anxiety", "Muscle spasms", "Headaches", "Migraines", "Nausea"],
        ["Stress", "Anxiety", "Bad Moods", "Sleep Deprivation", "Pain", "Appetite", "Focus", "Nausea", "Inflammation"],
        ["Headaches", "Muscle Tension", "Insomnia", "Depression", "Inflammation", "Appetite", "Stress", "Cramps", "Lack of Creativity"],
        ["Anxiety", "Stress", "Sour Moods", "Pain", "Sleep Deprivation", "Appetite Loss", "Nausea", "Inflammation", "Lack of focus"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Loss of appetite"],
        ["Pain", "Insomnia", "Depression", "Anxiety", "Inflammation", "Headaches", "Nausea"],
        ["Stress", "Anxiety", "Depression", "Insomnia", "Inflammation", "Chronic pain", "Headaches", "PTSD", "Nausea"],
        
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "Migraines", "PTSD"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Muscle spasms"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Muscle spasms", "Headaches"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Loss of appetite", "Muscle spasms"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Loss of appetite", "Muscle spasms", "Headaches"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Loss of appetite", "Muscle spasms", "Headaches", "Migraines"],
        ["Stress", "Anxiety", "Depression", "Insomnia", "Inflammation", "Chronic pain", "Headaches", "PTSD", "Nausea", "Muscle spasms"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Loss of appetite", "Muscle spasms", "Headaches", "Migraines", "Seizures"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Loss of appetite", "Muscle spasms", "Headaches", "Migraines", "Seizures", "Chronic pain"],
        ["Pain", "Anxiety", "Depression", "Insomnia", "Inflammation", "Nausea", "PTSD", "Loss of appetite", "Muscle spasms", "Headaches", "Migraines", "Seizures", "Chronic pain", "Epilepsy"],
        ['Pain', 'Inflammation', 'Stress', 'Anxiety', 'Depression', 'Nausea', 'Insomnia', 'Headaches'],
        ['Insomnia', 'Anxiety', 'Depression', 'Nausea', 'Stress', 'Discomfort', 'Painful cramps', 'Irritability'],
        ['Depression', 'Anxiety', 'Insomnia', 'Stress', 'Fatigue', 'Irritability', 'Lack of focus'],
        ['Inflammation', 'Pain', 'Nausea', 'Stress', 'Depression', 'Anxiety', 'Headaches'],
        ['Depression', 'Anxiety', 'Stress', 'Lack of focus', 'Nausea', 'Insomnia', 'Irritability'],
        ['Pain relief', 'Relaxation', 'Anti-anxiety', 'Anti-inflammatory', 'Headache relief', 'Nausea relief'],
        ['Inflammation', 'Pain', 'Anxiety', 'Depression', 'Insomnia', 'Fatigue', 'Lack of focus'],
        ['Anxiety', 'Depression', 'Nausea', 'Insomnia', 'Pain', 'Stress', 'Inflammation'],
        ['Inflammation', 'Pain', 'Stress', 'Anxiety', 'Nausea', 'Depression', 'Headaches'],
        ['Anxiety', 'Depression', 'Insomnia', 'Stress', 'Fatigue', 'Lack of focus', 'Nausea'],
        ['Stress', 'Anxiety', 'Depression', 'Pain', 'Inflammation', 'Nausea', 'Insomnia'],
        ['Pain', 'Anxiety', 'Depression', 'Nausea', 'Inflammation', 'Lack of focus', 'Insomnia'],
        ['Pain relief', 'Relaxation', 'Anti-anxiety', 'Anti-inflammatory', 'Headache relief', 'Nausea relief'],
        ['Inflammation', 'Pain', 'Anxiety', 'Depression', 'Insomnia', 'Fatigue', 'Lack of focus'],
        ['Stress', 'Depression', 'Anxiety', 'Insomnia', 'Nausea', 'Pain', 'Inflammation'],
        ['Pain', 'Anxiety', 'Depression', 'Nausea', 'Inflammation', 'Lack of focus', 'Insomnia'],
        ['Relaxation', 'Pain relief', 'Anti-inflammatory', 'Anti-anxiety', 'Stress relief', 'Headache relief'],
    ],
    "aromas": [
        ['Citrusy', 'Earthy', 'Herbal', 'Piney', 'Sweet'],
        ['Berry', 'Earthy', 'Fruity', 'Grape', 'Sweet'],
        ['Earthy', 'Flowery', 'Herbal', 'Pungent', 'Sweet'],
        ['Diesel', 'Earthy', 'Piney', 'Pungent', 'Sour', 'Spicy'],
        ['Citrusy', 'Earthy', 'Piney', 'Sour', 'Spicy'],
        ['Earthy', 'Herbal', 'Pungent', 'Sour', 'Sweet'],
        ['Earthy', 'Herbal', 'Piney', 'Spicy', 'Woody'],
        ['Earthy', 'Flowery', 'Pungent', 'Sour', 'Spicy'],
        ['Earthy', 'Fruity', 'Piney', 'Spicy', 'Sweet'],
        ['Earthy', 'Piney', 'Sweet', 'Woody'],
        ['Diesel', 'Earthy', 'Piney', 'Pungent', 'Sour', 'Woody'],
        ['Earthy', 'Herbal', 'Piney', 'Spicy', 'Sweet'],
        ['Diesel', 'Earthy', 'Piney', 'Pungent', 'Sweet'],
        ['Earthy', 'Herbal', 'Piney', 'Spicy', 'Woody'],
        ['Earthy', 'Piney', 'Spicy', 'Woody'],
        ['Earthy', 'Herbal', 'Piney', 'Sour', 'Sweet'],
        ['Pineapple', 'Blueberry', 'Earthy', 'Lemon'],
        ['Mango', 'Peppery', 'Diesel', 'Minty', 'Pine'],
        ['Grape', 'Spicy', 'Floral', 'Berry', 'Woody'],
        ['Lime', 'Sweet', 'Herbal', 'Skunky'],
        ['Orange', 'Gassy', 'Vanilla', 'Fruity'],
        ['Lavender', 'Citrus', 'Cheese', 'Nutty'],
        ['Strawberry', 'Minty', 'Earthy', 'Tropical'],
        ['Chocolate', 'Coffee', 'Hazelnut', 'Woody'],
        ['Apple', 'Rose', 'Ginger', 'Sour'],
        ['Honey', 'Apricot', 'Sage', 'Butter'],
        ['Cherry', 'Menthol', 'Tangy', 'Pungent', 'Chocolatey'],
        ['Bubblegum', 'Grassy', 'Cinnamon', 'Buttery'],
        ['Blackberry', 'Hops', 'Caramel', 'Earthy'],
        ['Grapefruit', 'Sandalwood', 'Sweet', 'Sour'],
        ['Peach', 'Spicy', 'Herbal', 'Earthy'],
        ['Citrus', 'Pine', 'Berry', 'Spicy'],
        ['Minty', 'Earthy', 'Floral', 'Woody', 'Sweet'],
        ['Fruity', 'Herbal', 'Peppery', 'Cheese'],
        ['Grape', 'Tropical', 'Vanilla', 'Nutty', 'Sour'],
        ['Skunky', 'Diesel', 'Sage', 'Butter'],
        ['Chocolate', 'Coffee', 'Honey', 'Lavender'],
        ['Ammonia', 'Apricot', 'Basil', 'Cherry', 'Chestnut'],
        ['Cinnamon', 'Coconut', 'Ginger', 'Haze'],
        ['Leather', 'Lemon', 'Lime', 'Mango'],
        ['Melon', 'Mint', 'Musty', 'Orange'],
        ['Peach', 'Pear', 'Rose', 'Sandalwood'],
        ['Strawberry', 'Tea', 'Thyme', 'Tropical'],
        ['Vanilla', 'Violet', 'Wine', 'Butterscotch'],
        ['Watermelon', 'Yeasty', 'Yogurt', 'Zesty'],
        ['Apple', 'Apricot', 'Cherry', 'Chocolaty'],
        ["Peppery", "Sweet", "Flowery", "Buttery"],
        ["Spicy", "Fruity", "Savory", "Minty"],
        ["Woody", "Earthy", "Nutty", "Minty"],
        ["Herbal", "Citrusy", "Piney", "Cheesy"]
    ],
    "composition": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
}

names = info_dict["names"]
short_descriptions = info_dict["descriptions"]
categories = info_dict["categories"]
prices = info_dict["prices"]
previous_prices = info_dict["previous_prices"]
effects = info_dict["effects"]
may_relieve = info_dict["may_relieve"]
aromas = info_dict["aromas"]
compositions = info_dict["composition"]

fixture = []
pk = 0

for index, name in enumerate(info_dict["names"]):
    replacements = ["Starry Night", "Mystic Haze", "Emerald Dream", "Purple Rain", "Sunburst Sativa", "Blueberry Bliss", "Northern Lights Reserve"]
    pk += 1
    image = f"images-to-use/products/{pk}.webp"
    description = """At our online cannabis store, we pride ourselves on offering only the highest quality products to our customers. Whether you're looking for premium flower strains, potent concentrates, delicious edibles, or smoking accessories, we have everything you need to enjoy the best possible cannabis experience.
\nOur products are carefully sourced from trusted suppliers and rigorously tested for quality and potency, so you can trust that you're getting the best possible cannabis products. With discreet and fast shipping options, you can enjoy your products in no time. Shop with us today and experience the best that the world of cannabis has to offer."""
    
    fixture.append({
      "model": "store.product",
      "pk": pk,
      "fields": {
        "name": name,
        "image": image,
        "short_description": short_descriptions[index],
        "description": description,
        "category": random.choice(categories),
        "price": prices[index],
        "previous_price": previous_prices[index],
        "effects": ", ".join(effects[index]),
        "may_relieve": ", ".join(may_relieve[index]),
        "aromas": ", ".join(aromas[index]),
        "composition": [random.choice(compositions), random.choice(compositions)]
      }
    })

with open("store/fixtures/products.json", "w") as products_fixture:
    products_fixture.write(json.dumps(fixture))



# [
#   {
#     "model": "store.product",
#     "pk": 1,
#     "fields": {
#       "name": "Purple Haze",
#       "image": "images-to-use/products/1.png",
#       "short_description": "A classic sativa strain",
#       "description": "Purple Haze is a classic sativa strain made popular by Jimi Hendrix's 1967 classic. This strain is known for its distinct aroma and uplifting effects. The buds are a bright green color and are covered in trichomes, giving them a frosty appearance. The taste is sweet and earthy, with a hint of grape.",
#       "category": 1,
#       "weights": "28g",
#       "price": 50.0,
#       "previous_price": 0.0,
#       "addons": [1, 2],
#       "effects": "Energetic, Creative, Happy",
#       "may_relieve": "Depression, Anxiety, Stress",
#       "aromas": "Earthy, Sweet, Grape",
#       "composition": [1, 2, 5, 7]
#     }
#   }
# ]

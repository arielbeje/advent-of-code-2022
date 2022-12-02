use std::fs;
use std::str::FromStr;

fn main() {
    let raw_day_input = fs::read_to_string("input.txt").expect("Couldn't read day input");
    let day_input = raw_day_input
        .strip_suffix('\n')
        .expect("Input is empty after stripping ending newline");

    let max_calorie_count = day_input
        .split("\n\n")
        .map(|block| -> u32 {
            block
                .split('\n')
                .map(|count| u32::from_str(count).expect("Failed to parse calorie count"))
                .sum()
        })
        .max()
        .expect("Couldn't find blocks split by 2 newlines");

    println!("{:?}", max_calorie_count);
}

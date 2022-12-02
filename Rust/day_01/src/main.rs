use std::fs;
use std::str::FromStr;

fn main() {
    let raw_day_input = fs::read_to_string("input.txt").expect("Couldn't read day input");
    let day_input = raw_day_input
        .strip_suffix('\n')
        .expect("Input is empty after stripping ending newline");

    let mut per_elf_calories: Vec<u32> = day_input
        .split("\n\n")
        .map(|block| -> u32 {
            block
                .split('\n')
                .map(|count| u32::from_str(count).expect("Failed to parse calorie count"))
                .sum()
        })
        .collect();
    per_elf_calories.sort_by(|a, b| b.cmp(a));

    let top_three_elves_calories: u32 = per_elf_calories
        .chunks_exact(3)
        .next()
        .expect("Couldn't find the top 3 elves")
        .iter()
        .sum();

    println!("{:?}", top_three_elves_calories);
}

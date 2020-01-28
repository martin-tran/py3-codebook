#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>

std::string to_lower(std::string s) {
  std::transform(s.begin(), s.end(), s.begin(),
		 [](unsigned char c) -> unsigned char { return std::tolower(c); });
  return s;
}

std::vector<std::vector<int>> init_backtables(const std::vector<std::string> &needles) {
  std::vector<std::vector<int>> backtables;

  // Preprocess the backtables for each of our needles.
  for (int i = 0; i < needles.size(); i++) {
    int n = needles[i].size();

    // Initialize our backtable for the i-th needle.
    std::vector<int> backtable;
    backtable.resize(n+1);
    backtable[0] = -1;

    int pos;
    for (int j = 1; j <= n; j++) {
      pos = backtable[j-1];
      while (pos != -1 && needles[i][j-1] != needles[i][pos])
	pos = backtable[pos];
      backtable[j] = pos + 1;
    }

    backtables.push_back(backtable);
  }

  return backtables;
}

std::vector<std::vector<int>> knuth_morris_pratt(const std::string &haystack,
						 const std::vector<std::string> &needles,
						 const std::vector<std::vector<int>> &backtables) {
  std::vector<std::vector<int>> matches;
  
  // Start searching through the text with each needle.
  for (int l = 0; l < needles.size(); l++) {
    auto needle = needles[l];
    std::vector<int> match;
    int i = 0, j = 0;

    while (i < haystack.size()) {
      while (j != -1 && (j == needle.size() || haystack[i] != needle[j]))
	j = backtables[l][j];
      i++;
      j++;
      if (j == needle.size())
	match.push_back(i - j);
    }
    matches.push_back(match);
  }

  return matches;  
}

std::vector<std::vector<int>> knuth_morris_pratt(const std::string &haystack,
						 const std::vector<std::string> &needles) {
  return knuth_morris_pratt(haystack, needles, init_backtables(needles));  
}

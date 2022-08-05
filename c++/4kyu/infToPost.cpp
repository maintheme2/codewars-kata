#include <string>
#include <stack>

using namespace std;

string tokenType(char token) {
  if (isdigit(token))
    return "number";
  else if ((token == '+') || (token == '^') || (token == '/') || (token == '*') || (token == '-')) 
    return "operation";
  else if (token == ')') 
    return "rightPar";
  else if (token == '(') 
    return "leftPar";
  return "";
}

int opPriority(char operation) {
  if ((operation == '+') || (operation == '-'))
    return 1;
  else if ((operation == '*') || (operation == '/'))
    return 2;
  else if (operation == '^')
    return 3;
  return -1;
}

string to_postfix(string infix) {

  stack<char> stack;
  string postfix;

  for (char token : infix) {
    if (tokenType(token) == "number") 
      postfix.push_back(token);
    else if (tokenType(token) == "leftPar")
      stack.push(token);
    else if (tokenType(token) == "rightPar") {
      while (tokenType(stack.top()) != "leftPar") { 
        postfix += stack.top();
        stack.pop();
      }
      stack.pop();
    }
    else {
      while (!stack.empty() && (opPriority(stack.top()) >= opPriority(token))) {
        postfix += stack.top();
        stack.pop();
      }
      stack.push(token);
    }
  }
  while (!stack.empty()) {
    postfix += stack.top();
    stack.pop();
  }
  return postfix;
}
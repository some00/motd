SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
sqlite3 -list $SCRIPT_DIR/quotes.sqlite 'SELECT formatted FROM quotes ORDER BY RANDOM() LIMIT 1;'

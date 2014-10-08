DROP TABLE IF EXISTS contact;
CREATE TABLE contact (
  contactId INTEGER PRIMARY KEY,
  firstName TEXT,
  lastName TEXT,
  phone TEXT,
  address TEXT,
  city TEXT,
  state TEXT,
  zip TEXT
);
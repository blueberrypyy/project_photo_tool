function generateEmails() {
      var at, counter, domain, dotpos, dotpos_over, email, email_list, new_email, user, user_list;
      email = document.getElementById("email-input").value;
      email_list = [email];
      domain = "$@.+\\.com^";
      at = email.indexOf("@");
      domain = email.slice(at);
      user = email.slice(0, at);
      new_email = "";
      counter = 0;
      dotpos = 0;

      for (var i = 0, _pj_a = user.length - 1; i < _pj_a; i += 1) {
        user_list = Array.from(user);
        dotpos += 1;
        user_list.splice(dotpos, 0, ".");
        new_email = user_list.join("") + domain;

        if (dotpos > user_list.length - 1) {
          console.log("Full");
        } else {
          email_list.push(new_email);
        }
      }

      document.getElementById("email-output").value = email_list.join("\n");
    }


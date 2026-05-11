func BeginRegistration(w http.ResponseWriter, r *http.Request) {
			// ①
		registerOptions := func(credCreationOpts *protocol.PublicKeyCredentialCreationOptions) {
			credCreationOpts.CredentialExcludeList = user.CredentialExcludeList()
		}
		..
		// ②
		options, sessionData, err := Wc.BeginRegistration(
			user,
			registerOptions,
		)
	}